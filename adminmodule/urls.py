from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('properties/', views.propertieshomepage, name='propertieshomepage'),
    path('agents/', views.agentshomepage, name='agentshomepage'),
    # Add more URL patterns as needed
]
