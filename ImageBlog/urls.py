from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('HomePage.urls')),
    path('user/', include('UserPage.urls')),
    path('admin/', admin.site.urls),
]
