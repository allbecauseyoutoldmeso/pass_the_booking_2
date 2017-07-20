from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.client_list, name='client_list'),
    url(r'^client/(?P<pk>\d+)/$', views.client_detail, name='client_detail'),
    url(r'^client/new/$', views.client_new, name='client_new'),
    url(r'^client/(?P<pk>\d+)/edit/$', views.client_edit, name='client_edit'),
    url(r'^properties/$', views.properties, name='properties'),
    url(r'^properties/(?P<pk>\d+)/$', views.property_detail, name='property_detail'),
    url(r'^client/(?P<pk>\d+)/properties/new/$', views.property_new, name='property_new'),
]
