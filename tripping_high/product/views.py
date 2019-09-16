# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .apis import Category, Product


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
