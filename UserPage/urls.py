from django.urls import path
from . import views

app_name = 'UserPage'

urlpatterns = [
    path('add-blog/', views.AddBlog, name='AddBlog'),
    path('edit-profile/', views.EditProfile, name='EditProfile'),
    path('', views.Profile, name='Profile'),
]
