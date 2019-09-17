from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^category/(?P<cid>[0-9])/$', views.category, name='api-category'),
    url(r'^category/$', views.category, name='api-category'),
    url(r'^variant/(?P<vid>[0-9])/$', views.variant, name='variant'),
    url(r'^variant/$', views.variant, name='variant'),
    url(r'^$', views.product, name='api-product'),
    url(r'^(?P<pid>[0-9])/$', views.product, name='api-product'),
    url(r'^(?P<slug>[-\w]+)/$', views.productPage, name='product'),
    
]