from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hunterbuild/$', views.hunter_build, name='hunter_build'),
    url(r'^hunterbuild/(?P<pk>\d+)/$', views.hunterbuild_detail, name='hunterbuild_detail'),
    url(r'^hunterbuild/new/$', views.hunter_new, name='hunter_new'),
    url(r'^hunterbuild/delete/(?P<pk>\d+)/$', views.deletehunter, name='deletehunter'),
]
