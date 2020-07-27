
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index),
    path(r'users/', views.users, name='users'),
]
