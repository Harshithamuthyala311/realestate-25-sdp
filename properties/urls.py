# agents/urls.py
from django.urls import path
from .views import viewproperty_listing

urlpatterns = [
    path('viewproperty_listing/', viewproperty_listing, name='viewproperty_listing'),
]
