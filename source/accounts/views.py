from urllib.parse import urlencode

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


from accounts.forms import SignUpForm

NEXT_URL = ''
def login_view(request):
    context = {}
    if request.method == 'GET':
        global NEXT_URL
        NEXT_URL = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if NEXT_URL == None:
                return redirect('issue_list')
            return redirect('http://localhost:8000' + NEXT_URL)
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('issue_list')

def register_view(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'register.html', context={'form':form})
    elif request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data.get('username'))
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('issue_list')
        else:
            return render(request, 'register.html', context={'form': form})