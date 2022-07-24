
from django.urls import path

from mini2app import views

urlpatterns = [
    path('test/', views.test),
    path('first/', views.first_Screen),
    path('songpa/', views.songpa),
]
