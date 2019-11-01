from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# from accounts.models import Profile
from accounts.models import Profile


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

class UserChangeForm(forms.ModelForm):
    git_repo = forms.CharField(label='Ссылка на репозиторий GIT', max_length=120, required=False)
    avatar = forms.ImageField(label='Аватар', required=False)
    birth_date = forms.DateField(label='День рождения', input_formats=['%Y-%m-%d', '%d.%m.%Y'], required=False)

    def get_initial_for_field(self, field, field_name):
        if field_name in self.Meta.profile_fields:
            return getattr(self.instance.profile, field_name)
        return super().get_initial_for_field(field, field_name)

    def save(self, commit=True):
        user = super().save(commit)
        self.save_profile(commit)
        return user

    def save_profile(self, commit=True):
        profile = Profile.objects.get_or_create(user=self.instance)[0]
        for field in self.Meta.profile_fields:
            setattr(profile, field, self.cleaned_data[field])
        if not profile.avatar:
            profile.avatar = 'user_pics/765-default-avatar.png'
        if commit:
            profile.save()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','avatar','birth_date','git_repo']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}
        profile_fields = ['avatar', 'birth_date', 'git_repo']

    # def __init__(self, *args, **kwargs):
    #     super(UserChangeForm, self).__init__(*args, **kwargs)
    #     self.fields['git_repo'] = 'lala'


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label="Новый пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label="Старый пароль", strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неправильный!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password']



