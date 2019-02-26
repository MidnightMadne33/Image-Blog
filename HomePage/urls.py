from django.urls import path
from . import views

app_name = 'HomePage'

urlpatterns = [
    path('signin/', views.SignIn, name='SignIn'),
    path('signup/', views.SignUp, name='SignUp'),
    path('signout/', views.SignOut, name='SignOut'),
    path('', views.Index, name='Index'),
]
