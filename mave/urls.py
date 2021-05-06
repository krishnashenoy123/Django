from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Mave-Home'),
    path('about/', views.about, name='Mave-About'),
]