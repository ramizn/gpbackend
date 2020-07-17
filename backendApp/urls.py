from django.urls import path

from . import views

urlpatterns = [
    path('', views.login),
    path('getoptimal', views.getOptimalPath),
    path('signup', views.signup)
]