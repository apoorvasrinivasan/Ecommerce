from .models import Category as Cat, Product as P, Variant as V
from django.http import HttpResponseBadRequest

class Generic(object):
  def __init__(self,request,  return_type = 'raw',*args,**kwargs):
    self.method = request.method
    self.return_type = return_type

  def ret(self):
    if self.return_type == 'raw':
      return self.obj
    elif self.return_type == 'dict':
      return self.get_dict()
    elif self.return_type == 'json':
      return self.get_json()

  def get_dict(self):
    if isinstance( self.obj,self.model):
      f =  self.obj.dict()
    else:
      f = []
      for c in self.obj:
        f.append(c.dict())
    return f
  def get(self, pk = None,**kwargs):
    if pk:
      try:
        self.obj = self.model.objects.get(pk =int(pk))
      except:
        raise HttpResponseBadRequest
    elif kwargs:
      self.obj = self.model.objects.get(**kwargs)
    else:
      self.obj = self.model.objects.all()
    return self.ret()


class Category(Generic):

  def __init__(self,request,*args,**kwargs):
    self.model = Cat
    super(Category, self).__init__( request, *args, **kwargs)
    
  


class Product(Generic):
  def __init__(self,request,*args,**kwargs):
    self.model = P
    super(Product, self).__init__( request, *args, **kwargs)
  # def get_filtered(self):
  #   p = self.obj
  #   filters= {}
  #   for r in request.GET.keys():
  #     filters[r] = request.GET.get(r)

    
class Variant(Generic):
  def __init__(self,request,*args,**kwargs):
    self.model = V
    super(Variant, self).__init__( request, *args, **kwargs)
    

