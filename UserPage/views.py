from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.decorators import login_required


def Profile(request):
    #user profile info
    return render(request, 'UserPage/Profile.html')


def EditProfile(request):
#     form = UserProfileForm()
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST)
#         if form.is_valid():
#             form.save()
    return render(request, 'UserPage/EditProfile.html')


@login_required(login_url='/signin/')
def AddBlog(request):

    return render(request, 'UserPage/AddBlog.html')
