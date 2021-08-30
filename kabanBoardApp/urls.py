from . import views
from django.urls import path

urlpatterns = [
    path('newcard/', views.newcard, name='newcard'),
    path('home/', views.home, name='home'),
    path('', views.login, name='login'),
    path('logout/', views.login, name='logout'),
]