from urllib.parse import urlencode

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


from accounts.forms import SignUpForm

def login_view(request):
    context = {}
    if request.method == 'GET':
        global NEXT_URL
        next_url = request.GET.get('next', '')
        context['next'] = next_url
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
        else:
            context['next'] = next_url
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