from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^index', views.index, name="index"),
    url(r'^login', views.login, name="login"),
    url(r'^register', views.register, name="register"),
    url(r'^menu', views.menu, name="menu"),
    url(r'^light_add', views.light_add, name="light_add"),
    url(r'^light_index', views.light_index, name="light_index"),
    url(r'^light_control', views.light_form, name="light_control"),
    url(r'^light_single', views.light_single, name="light_single"),
    url(r'^light_managment', views.light_managment, name="light_managment"),
    url(r'^group_add', views.group_add, name="group_add"),
    url(r'^group_managment', views.group_managment, name="group_managment"),
    url(r'^single/', views.light_single, name="light_single")
]


