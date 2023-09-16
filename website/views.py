from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for coral reef"""
    return render(request, 'website/index.html')

def coral_reef(request):
    """Coral reef page"""
    return render(request, 'website/coral_reef.html')

def help_the_ocean(request):
    return render(request, 'website/help_the_ocean.html')