from django.conf.urls import include, url

from . import views

urlpatterns =[
	url(r'^$', views.index, name='index'),
	url(r'^(?P<flat_floor_id>[0-9]+)/$', views.floor, name='floors'),
	url(r'^(?P<flat_floor_id>[0-9]+)/(?P<flat_number>[a-z0-9]+)/$', views.flat, name='flat'),
	url(r'^(?P<flat_floor_id>[0-9]+)/(?P<flat_number>[a-z0-9]+)/application/confirmation/$', views.apply, name='apply'),
]