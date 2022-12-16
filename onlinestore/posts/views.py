from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def main_view(request):
    return render(request, 'posts/index.html')

def products_view(request):
    return render(request, 'posts/products.html')


