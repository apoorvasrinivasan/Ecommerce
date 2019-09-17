# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .apis import Category, Product, Variant
from .models import VariantValues, Product as P


# Create your views here.
def category(request, cid =None):
	c = Category(request,return_type='dict')
	c = c.get(cid)
	
	return JsonResponse(c, safe = False)
# Create your views here.
def product(request, pid =None):
	p = Product(request,return_type='dict')
	p = p.get(pid)
	return JsonResponse(p, safe = False)

def variant(request, vid =None):
	p = Variant(request,return_type='dict')
	p = p.get(vid)
	return JsonResponse(p, safe = False)

def product_listing(request):
	filtters = []
	cat = None;
	for r in request.GET.keys():
		if r == 'category':
			cat = request.GET.get('category', None)
		else:
			filtters.append(request.GET.get(r))
	print filtters
	
	v =VariantValues.objects.filter(value__in = filtters).values_list('product')
	kwargs = {}
	if v:
		kwargs['pk__in'] = v

	if cat:
		kwargs['category__name__iexact'] = cat
	p = P.objects.filter( **kwargs)
	pros = []
	for pp in p:
		pros.append(pp.dict())

	return 	render(request, 'product_listing.pug', {'products':pros})

def productPage(request, slug):
	p = Product(request, 'dict')
	p = p.get(slug = slug)
	return 	render(request, 'product.pug', {'product':p})

