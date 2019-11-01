from urllib.parse import urlencode

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ImproperlyConfigured
from django.db import transaction
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView

from accounts.models import Token, Profile
from main.settings import HOST_NAME

from accounts.forms import SignUpForm, UserChangeForm, PasswordChangeForm  # ProfileForm


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
            Profile.objects.create(user=user)
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


    # def get_form(self, form_class=None):
    #     if self.request.method == 'GET':
    #         form = UserChangeForm()
    #         cur_user = User.objects.get(username=self.request.user)
    #         form.fields['first_name'].initial = cur_user.first_name
    #         form.fields['last_name'].initial = cur_user.last_name
    #         form.fields['email'].initial = cur_user.email
    #         form.fields['git_repo'].initial = Profile.objects.filter(user=self.request.user).get().git_repo
    #         return form
    #     form_class = super().get_form_class()
    #     return form_class(**self.get_form_kwargs())
    #
    # def form_valid(self, form):
    #     self.object = form.save()
    #     cur_user = User.objects.get(pk=self.object.pk)
    #     try:
    #         user_profile = Profile.objects.get(user=cur_user)
    #     except:
    #         user_profile = None
    #     if user_profile == None:
    #         Profile.objects.create(
    #             user=cur_user,
    #             git_repo=form.cleaned_data.get('git_repo')
    #         ).save()
    #     else:
    #         user_profile.git_repo = form.cleaned_data.get('git_repo')
    #         user_profile.save()
    #     return super().form_valid(form)

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