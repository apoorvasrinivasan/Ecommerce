from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^category/(?P<cid>[0-9])/$', views.category, name='category'),
    url(r'^category/$', views.category, name='category'),
    url(r'^$', views.product, name='product'),
    url(r'^(?P<pid>[0-9])/$', views.product, name='product'),
]
