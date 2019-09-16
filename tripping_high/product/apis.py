from .models import Category as Cat, Product as P
from django.http import HttpResponseBadRequest

class Generic(object):
  def __init__(self,request,*args,**kwargs):
    self.method = request.method
    self.return_type = kwargs['return_type'] if 'return_type' in kwargs else 'raw'

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
    

