"""Defines url patterns for Coral Reef Website"""

from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('coral_reef/', views.coral_reef,name='coral_reef'),
    path('help_the_ocean/', views.help_the_ocean,name='help_the_ocean'),
    path('reviews/', views.reviews, name='reviews'),
]