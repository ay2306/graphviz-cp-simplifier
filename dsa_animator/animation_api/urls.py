from django.contrib import admin
from django.urls import path
from animation_api import views

urlpatterns = [
    path('', views.home, name='animate_api-animate-home'),
    path('<str:animation_name>', views.create_animation_by_name, name='animate_api-create_animation_by_name'),
]
