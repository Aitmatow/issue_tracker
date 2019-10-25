from urllib.parse import urlencode

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

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
            return redirect('http://localhost:8000' + NEXT_URL)
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('issue_list')