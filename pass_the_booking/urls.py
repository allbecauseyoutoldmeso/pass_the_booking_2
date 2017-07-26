from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^clients/$', ClientListView.as_view(), name='client_list'),
    url(r'^clients/(?P<pk>\d+)/$', ClientDetailView.as_view(), name='client_detail'),
    url(r'^clients/new/$', ClientCreate.as_view(), name='client_new'),
    url(r'^clients/(?P<pk>\d+)/edit/$', ClientUpdate.as_view(), name='client_edit'),
    url(r'^clients/(?P<pk>\d+)/delete/$', ClientDelete.as_view(), name='client_delete'),
    url(r'^properties/$', PropertyListView.as_view(), name='property_list'),
    url(r'^properties/(?P<pk>\d+)/$', PropertyDetailView.as_view(), name='property_detail'),
    url(r'^clients/(?P<pk>\d+)/properties/new/$', PropertyCreate.as_view(), name='property_new'),
    url(r'^properties/(?P<pk>\d+)/edit/$', PropertyUpdate.as_view(), name='property_edit'),
    url(r'^properties/(?P<pk>\d+)/delete/$', PropertyDelete.as_view(), name='property_delete'),
    url(r'^properties/(?P<pk>\d+)/bookings/new/$', BookingCreate.as_view(), name='booking_new'),
    url(r'^bookings/(?P<pk>\d+)/$', BookingDetailView.as_view(), name='booking_detail'),
    url(r'^bookings/(?P<pk>\d+)/edit/$', BookingUpdate.as_view(), name='booking_edit'),
    url(r'^bookings/(?P<pk>\d+)/delete/$', views.booking_delete, name='booking_delete'),
    url(r'^bookings/$', BookingListView.as_view(), name='booking_list'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
