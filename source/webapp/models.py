from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

DEFAULT_PROJECT_STATUS = 'active'
PROJECT_STATUS_CHOICES = [(DEFAULT_PROJECT_STATUS, 'Активен'), ('closed', 'Закрыт')]

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=4000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('Statuses', related_name='issues', on_delete=models.PROTECT, null=True, blank=True,
                               verbose_name='Тип статуса')
    tip = models.ForeignKey('Tips', related_name='issues', on_delete=models.PROTECT, null=True, blank=True,
                            verbose_name='Тип задачи')
    project = models.ForeignKey('Projects', related_name='issues', on_delete=models.PROTECT, null=True, blank=False,
                                verbose_name='Проект' )
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    created_by = models.ForeignKey(User, related_name='issues', on_delete=models.PROTECT, null=True, blank=False,
                                   verbose_name='Автор задачи')
    assigned_to = models.ForeignKey(User, related_name='ussues', on_delete=models.PROTECT, null=True, blank=False,
                                    verbose_name='Исполнитель задачи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задачу'


class Statuses(models.Model):
    name = models.CharField(max_length=20, verbose_name='Статус')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('statuses_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Статус'
        verbose_name = 'Статусы'

class Tips(models.Model):
    name = models.CharField(max_length=20, verbose_name='Тип')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tips_edit', kwargs={'pk':self.pk})

    class Meta:
        verbose_name_plural = 'Тип'
        verbose_name = 'Типы'

class Projects(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False, verbose_name='Название проекта')
    description = models.TextField(max_length=4000, null=True, blank=True, verbose_name='Описание проекта')
    status = models.CharField(max_length=20, null=True, default=DEFAULT_PROJECT_STATUS, blank=False, verbose_name='Статус проекта',
                              choices=PROJECT_STATUS_CHOICES)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Проект'
        verbose_name = 'Проекты'