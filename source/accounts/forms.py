from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label='Логин')
    first_name = forms.CharField(max_length=100, required=False, label='Имя')
    last_name = forms.CharField(max_length=100, required=False, label='Фамилия')
    password = forms.CharField(max_length=100, required=True, label='Пароль', widget=forms.PasswordInput)

    password_confirm = forms.CharField(max_length=100, required=True, label='Подтверждение пароля', widget=forms.PasswordInput)
    email = forms.EmailField(required=True, label='Email')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('Username already taken.', code='username_taken')
        except User.DoesNotExist:
            return username

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_confirm')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if first_name == '' and last_name == '':
            raise ValidationError('One of the first name or last name should be filled', code='name_is_poll')
        if password_1 != password_2:
            raise ValidationError('Passwords do not match.', code='password_do_not_match')
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('Email already taken.', code='email_registered')
        except User.DoesNotExist:
            return email


