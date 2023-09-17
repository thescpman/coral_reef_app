from django.shortcuts import render
from .models import Review
# Create your views here.

def index(request):
    """The home page for coral reef"""
    return render(request, 'website/index.html')

def coral_reef(request):
    """Coral reef page"""
    return render(request, 'website/coral_reef.html')

def help_the_ocean(request):
    return render(request, 'website/help_the_ocean.html')

def reviews(request):

    reviews = Review.objects.all()
    context = {'reviews':reviews}
    return render(request, 'website/reviews.html', context)