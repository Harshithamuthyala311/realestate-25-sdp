# agents/views.py
from django.shortcuts import render

def viewproperty_listing(request):
    return render(request, 'properties/viewproperty_listing.html')
