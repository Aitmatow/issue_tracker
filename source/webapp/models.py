from django.db import models
from django.urls import reverse

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=4000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('Statuses', related_name='issues', on_delete=models.PROTECT, null=True, blank=True,
                               verbose_name='Тип статуса')
    tip = models.ForeignKey('Tips', related_name='issues', on_delete=models.PROTECT, null=True, blank=True,
                            verbose_name='Тип задачи')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title



class Statuses(models.Model):
    name = models.CharField(max_length=20, verbose_name='Статус')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('statuses_edit', kwargs={'pk': self.pk})


class Tips(models.Model):
    name = models.CharField(max_length=20, verbose_name='Тип')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tips_edit', kwargs={'pk':self.pk})
