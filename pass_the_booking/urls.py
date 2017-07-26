from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^clients/$', ClientListView.as_view(), name='client_list'),
    url(r'^clients/(?P<pk>\d+)/$', ClientDetailView.as_view(), name='client_detail'),
    url(r'^clients/new/$', ClientNewView.as_view(), name='client_new'),
    url(r'^clients/(?P<pk>\d+)/edit/$', views.client_edit, name='client_edit'),
    url(r'^clients/(?P<pk>\d+)/delete/$', views.client_delete, name='client_delete'),
    url(r'^properties/$', views.property_list, name='property_list'),
    url(r'^properties/(?P<pk>\d+)/$', views.property_detail, name='property_detail'),
    url(r'^clients/(?P<pk>\d+)/properties/new/$', views.property_new, name='property_new'),
    url(r'^properties/(?P<pk>\d+)/edit/$', views.property_edit, name='property_edit'),
    url(r'^properties/(?P<pk>\d+)/delete/$', views.property_delete, name='property_delete'),
    url(r'^properties/(?P<pk>\d+)/bookings/new/$', views.booking_new, name='booking_new'),
    url(r'^bookings/(?P<pk>\d+)/$', views.booking_detail, name='booking_detail'),
    url(r'^bookings/(?P<pk>\d+)/edit/$', views.booking_edit, name='booking_edit'),
    url(r'^bookings/(?P<pk>\d+)/delete/$', views.booking_delete, name='booking_delete'),
    url(r'^bookings/$', views.booking_list, name='booking_list'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
