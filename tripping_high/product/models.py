# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.text import slugify
from django.db import models

# Create your models here.
class ProductType(models.Model):
    """Type of product - >tshirts, bags, badges, pens etc"""
    title = models.CharField(max_length=120)
    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    """Type of product - >tshirts, bags, badges, pens etc"""
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    def dict(self):
        return {
            'name':self.name,
            'id':self.id,
            'slug':self.slug
        }
    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Category,self).save()

class Product(models.Model):
    sku = models.CharField(max_length=30)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, null=True, blank=True)
    pType = models.ForeignKey(ProductType)
    category = models.ForeignKey(Category)
    price = models.PositiveSmallIntegerField()
    created_on = models.DateField(auto_now_add=True)
    last_modified_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
 
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Product, self).save(*args, **kwargs)
    def dict(self):
        variants = self.productvariant_set.all().values('variantvalues__value', 'variantname__name')
        v = {}
        for x in variants:
            name =x['variantname__name']
            if name in v:
                v[name].append(x['variantvalues__value'])
            else:
                v[name]=[x['variantvalues__value']]

        return {
            'sku':self.sku,
            'title':self.title,
            'id':self.id,
            'slug':self.slug,
            'type':self.pType.title,
            'variants':v,
            'category':self.category.name,
            'category_full':self.category.dict(),
            'price':self.price,
            'created_on':self.created_on
        }

class Variant(models.Model):
    forType = models.ForeignKey(ProductType)
    name = models.CharField(max_length=50)
    default = models.CharField(max_length=50)
    options = models.CharField(max_length=50, help_text = 'comma separated options', null=True, blank=True)
    def __str__(self):
        return self.name
    def dict(self):
        return {
            "forType":self.forType.title,
            "name":self.name,
            "default":self.default,
            "options":self.options.split(',')   
        }

def variant_default(self):
        return self.variantname.default
def price_default(self):
        return self.product.price


class ProductVariant(models.Model):
    product = models.ForeignKey(to=Product)
    variantname = models.ManyToManyField(Variant, through='VariantValues')
    qnty = models.PositiveSmallIntegerField(default = 100)
    price = models.PositiveSmallIntegerField(blank = True, null = True)
    def __str__(self):
        return "Variants for %s "%(self.product.title)


class VariantValues(models.Model):
    product = models.ForeignKey(ProductVariant)
    variantname = models.ForeignKey(Variant)
    value = models.CharField(max_length=30, blank = True, null = True)
    def save(self,*args, **kwargs):
        if self.value is None:  
            self.value = self.variantname.default
        else:
            assert self.value in self.variantname.options.split(',')
        # if self.price is None:
        #     self.price = self.product.price
        super(VariantValues, self).save(*args, **kwargs)
        pass
    

    def __str__(self):
        return "%s - %s "%(self.product.product.title, self.value)
