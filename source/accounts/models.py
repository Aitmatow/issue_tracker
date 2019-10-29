from django.contrib.auth.models import AbstractUser, PermissionsMixin, User
from django.db import models
from uuid import uuid4
from django.conf import settings
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Token(models.Model):
    token = models.UUIDField(verbose_name='Token', default=uuid4())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='registration_tokens', verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.token)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    git_repo = models.CharField(max_length=125,verbose_name='Ссылка на репозиторий', blank=True)

    # @receiver
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender = User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    def __str__(self):
        return str(self.user.username)

