from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    UserBio = models.TextField(max_length=100)
    ProfileImage = models.ImageField(upload_to='ProfilePics', blank=True)

    def __str__(self):
        return self.user.username

    def name(self):
        return self.user.first_name + self.user.last_name


class Blog(models.Model):

    TextContent = models.TextField()
    ImageContent = models.ImageField(upload_to='UserMedia/User')
    Date = models.DateField(auto_now_add=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title
