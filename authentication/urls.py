from django.urls import path
from .views import *
urlpatterns = [
    path('', muestra, name='main'),
]