from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
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

def new_review(request):

    if request.method != 'POST':
        #No data submitted; create a blank form
        form = ReviewForm()
    else:
        #Post data submitted; process data
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:reviews')
        
    context = {'form':form}
    return render(request, 'website/new_review.html', context)