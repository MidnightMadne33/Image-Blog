from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    UserBio = models.TextField(max_length=100)
    ProfileImage = models.ImageField(upload_to='ProfilePics', blank=True)

    def __str__(self):
        return self.user.username

# class Blog(models.Model):
#     Title = models.CharField(max_length=50)
#     TextContent = models.TextField()
#     Date = models.DateField(auto_now_add=True)
#     Author
