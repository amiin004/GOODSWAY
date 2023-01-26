from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('login1', views.login1, name='login1'),
    path('admin', views.admin, name='admin'),
    path('rdriver',views.rdriver, name='rdriver'),
    path('rtruck', views.rtruck, name='rtruck'),
    path('driver', views.driver, name='driver'),
    path('feedback', views.feedback, name='feedback'),
    path('customer', views.customer, name='customer'),
    path('otruck', views.otruck, name='otruck'),
    path('vorders', views.vorders, name='vorders'),
    path('cusrating', views.cusrating, name='cusrating'),
    path('vrating', views.vrating, name='vrating'),
    path('pop', views.pop, name='pop'),
    path('ordersh', views.ordersh, name='ordersh'),
    path('otruckpop', views.otruckpop, name='otruckpop')
]