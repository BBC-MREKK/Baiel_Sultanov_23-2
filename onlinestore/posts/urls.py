
from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view),
    path('date/', products_view),
]