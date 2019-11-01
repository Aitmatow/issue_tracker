from django.contrib.auth.models import AbstractUser, PermissionsMixin, User
from django.db import models
from uuid import uuid4
from django.conf import settings
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from webapp.models import Projects


class Token(models.Model):
    token = models.UUIDField(verbose_name='Token', default=uuid4())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='registration_tokens', verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.token)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    about_me = models.TextField(max_length=3000, null=True, blank=False, verbose_name='О себе')
    git_repo = models.CharField(max_length=125,verbose_name='Ссылка на репозиторий', blank=True)

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Teams(models.Model):
    user = models.ForeignKey(User, related_name='teams',on_delete=models.PROTECT, null=True, blank=True, verbose_name='Пользователь')
    project = models.ForeignKey(Projects, related_name='teams', on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.project.name

    class Meta:
        verbose_name_plural = 'Команды'
        verbose_name = 'Команда'