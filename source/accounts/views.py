from urllib.parse import urlencode

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView

from accounts.models import Token
from main.settings import HOST_NAME

from accounts.forms import SignUpForm, UserChangeForm, PasswordChangeForm    # ProfileForm


def login_view(request):
    context = {}
    if request.method == 'GET':
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
            return redirect('issue_list')
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
            user = User(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                is_active=False
            )
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            token = Token.objects.create(user=user)
            activation_url = HOST_NAME + reverse('accounts:user_activate', kwargs={'token':token})
            print(activation_url)
            try:
                user.email_user('Вы зарегистрировались на сайте localhost:8000.',
                                'Для активации перейдите по ссылке: ' + activation_url)
            except ConnectionRefusedError:
                print('Could not send email.Server error.')
            return redirect('issue_list')
        else:
            return render(request, 'register.html', context={'form': form})

def user_activation_view(request,token):
    token = get_object_or_404(Token,token=token)
    user = token.user
    user.is_active = True
    user.save()
    login(request, user)
    return redirect('issue_list')

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

class UserPersonalInfoChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_info_change.html'
    form_class = UserChangeForm
    context_object_name = 'user_obj'

    # def update_profile(self,request):
    #     if request.method == 'POST':
    #         user_form = UserChangeForm(request.POST, instance=self.request.user)
    #         profile_form = ProfileForm(request.POST, instance=self.request.user.profile)
    #         if user_form.is_valid() and profile_form.is_valid():
    #             user_form.save()
    #             profile_form.save()
    #             return redirect('accounts:detail',pk=self.object.pk)
    #     else:
    #         user_form = UserChangeForm(instance=self.request.user)
    #         profile_form = ProfileForm(instance=self.request.user.profile)
    #     return render(self.request, 'user_info_change.html', {
    #         'user_form' : user_form,
    #         'profile_form' : profile_form
    #     })


    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.pk})

class UserPasswordChangeView(UserPassesTestMixin,UpdateView):
    model = User
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:login')

class UsersList(ListView):
    template_name = 'users_list.html'
    model = User
    paginate_by = 5
    paginate_orphans = 1
    page_kwarg = 'page'