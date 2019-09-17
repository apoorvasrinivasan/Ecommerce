# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from product.apis import Category, Variant

# Create your views here.

def index(request):
  # c = Category(request)
  # c = c.get()

  v = Variant(request, return_type= "dict")
  v = v.get()
  return render(request, 'index.pug',{"variants":v, 'images':['0','1','2']})