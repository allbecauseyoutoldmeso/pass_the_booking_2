from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.client_list, name='client_list'),
    url(r'^post/(?P<pk>\d+)/$', views.client_detail, name='client_detail'),
]
