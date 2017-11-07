from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^laboratorio/nuevo/$', views.lab_nuevo, name='lab_nuevo'),
    url(r'^evento/nuevo/$', views.evento_nuevo, name='evento_nuevo'),
    url(r'^$', views.post_list),
    url(r'^laboratorio/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^laboratorio/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^laboratorio/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    ]
