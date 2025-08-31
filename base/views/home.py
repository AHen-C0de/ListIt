#from django.shortcuts import render
from django.views.generic import ListView

from base.models import List

class HomeView(ListView):
    template_name='base/home.html'
    model = List
    context_object_name = "lists"