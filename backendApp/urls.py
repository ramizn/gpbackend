from django.urls import path

from . import views

urlpatterns = [
    path('getoptimal', views.getOptimalPath),
]