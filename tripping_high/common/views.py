# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from product.apis import Category

# Create your views here.

def index(request):
	c = Category(request)
	c = c.get()
	return render(request, 'index.pug',{'categories':c, 'images':['0','1','2']})