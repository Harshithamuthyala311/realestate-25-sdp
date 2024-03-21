from django.shortcuts import render

# Create your views here.

def projecthomepage(request):
    return render(request, 'projecthomepage.html')

def propertieshomepage(request):
    return render(request, 'propertieshomepage.html')

def agentshomepage(request):
    return render(request, 'agentshomepage.html')
