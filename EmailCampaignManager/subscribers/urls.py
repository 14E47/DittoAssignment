from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribeform/', views.subscribeform, name='subscribeform'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('unsubscribeform/', views.unsubscribeform, name='unsubscribeform'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
]
