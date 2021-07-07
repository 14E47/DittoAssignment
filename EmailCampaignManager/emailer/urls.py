from django.urls import path
from . import views

urlpatterns = [
    path('sendmailer', views.schedule_email, name='sendemailer'),
]
