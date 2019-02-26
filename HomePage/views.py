from django.shortcuts import render, redirect
from .forms import SignUpForm
from UserPage.models import UserProfile
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def Index(request):
    return render(request, 'HomePage/Index.html')


def SignIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('UserPage:Profile')
    else:
        form = AuthenticationForm()
    return render(request, 'HomePage/SignIn.html', {'forms':form})


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next', ''))
            else:
                return redirect('UserPage:Profile')
    else:
        form = SignUpForm()
    return render(request, 'HomePage/SignUp.html', {'forms':form})


def SignOut(request):
    if request.method == 'POST':
        logout(request)
        return redirect('HomePage:Index')
