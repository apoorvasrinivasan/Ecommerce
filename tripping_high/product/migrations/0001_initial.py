# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-09-14 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, max_length=140, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, max_length=140, null=True, unique=True)),
                ('price', models.PositiveSmallIntegerField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('last_modified_on', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qnty', models.PositiveSmallIntegerField(default=100)),
                ('price', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('default', models.CharField(max_length=50)),
                ('forType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductType')),
            ],
        ),
        migrations.CreateModel(
            name='VariantValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=30, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductVariant')),
                ('variantname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Variant')),
            ],
        ),
        migrations.AddField(
            model_name='productvariant',
            name='variantname',
            field=models.ManyToManyField(through='product.VariantValues', to='product.Variant'),
        ),
        migrations.AddField(
            model_name='product',
            name='pType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductType'),
        ),
    ]
