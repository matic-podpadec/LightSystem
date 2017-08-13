from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^index', views.index, name="index"),
    url(r'^login', views.login, name="login"),
    url(r'^register', views.register, name="register"),
    url(r'^menu', views.menu, name="menu"),
    url(r'^light_control', views.light_control, name="control"),
]
