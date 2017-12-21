from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^favicon.ico$', RedirectView.as_view(url='/static/favicon/favicon.ico')),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^hunterbuild/$', views.hunter_build, name='hunter_build'),
    url(r'^hunterbuild/(?P<pk>\d+)/$', views.hunterbuild_detail, name='hunterbuild_detail'),
    url(r'^hunterbuild/new/$', views.hunter_new, name='hunter_new'),
    url(r'^hunterbuild/delete/(?P<pk>\d+)/$', views.deletehunter, name='deletehunter'),
    url(r'^assassinbuild/$', views.assassin_build, name='assassin_build'),
    url(r'^assassinbuild/(?P<pk>\d+)/$', views.assassinbuild_detail, name='assassinbuild_detail'),
    url(r'^assassinbuild/new/$', views.assassin_new, name='assassin_new'),
    url(r'^assassinbuild/delete/(?P<pk>\d+)/$', views.deleteassassin, name='deleteassassin'),
    url(r'^magebuild/$', views.mage_build, name='mage_build'),
    url(r'^magebuild/(?P<pk>\d+)/$', views.magebuild_detail, name='magebuild_detail'),
    url(r'^magebuild/new/$', views.mage_new, name='mage_new'),
    url(r'^magebuild/delete/(?P<pk>\d+)/$', views.deletemage, name='deletemage'),
    url(r'^warriorbuild/$', views.warrior_build, name='warrior_build'),
    url(r'^warriorbuild/(?P<pk>\d+)/$', views.warriorbuild_detail, name='warriorbuild_detail'),
    url(r'^warriorbuild/new/$', views.warrior_new, name='warrior_new'),
    url(r'^warriorbuild/delete/(?P<pk>\d+)/$', views.deletewarrior, name='deletewarrior'),
    url(r'^guardianbuild/$', views.guardian_build, name='guardian_build'),
    url(r'^guardianbuild/(?P<pk>\d+)/$', views.guardianbuild_detail, name='guardianbuild_detail'),
    url(r'^guardianbuild/new/$', views.guardian_new, name='guardian_new'),
    url(r'^guardianbuild/delete/(?P<pk>\d+)/$', views.deleteguardian, name='deleteguardian'),
    url(r'^login/', auth_views.login, name='login_view'),
    url(r'^logout', views.logout_view, name='logout_view'),
    url(r'^signup/$', views.signup, name='signup'),
]
