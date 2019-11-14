from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import widgets

from accounts.models import Teams
from webapp.models import Issue, Statuses, Tips, Projects


class IssueForm(forms.ModelForm):
    created_by = forms.ModelChoiceField(queryset=User.objects.all(), label='Автор задачи', required=True, empty_label=None)
    assigned_to = forms.ModelChoiceField(queryset=None, label='Исполнитель задачи', required=True, empty_label=None)
    project = forms.ModelChoiceField(queryset=None, label='Проект', required=True, empty_label=None)


    # def __init__(self,*args,**kwargs):
    #     print(kwargs.values())
    #     super(IssueForm, self).__init__(*args, **kwargs)
    #     self.fields['created_by'].queryset = User.objects.filter(username='admin')


    class Meta:
        model = Issue
        exclude = ['']


class StatusForm(forms.ModelForm):
    # name = forms.CharField(max_length=20, required=True, label= 'Статус')

    class Meta:
        model = Statuses
        fields = ['name']



class TipsForm(forms.ModelForm):
    # name = forms.CharField(max_length=20, required=True, label='Тип')

    class Meta:
        model = Tips
        fields = ['name']

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['']

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class UserToProject(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), label='Пользователи', required=True)
    start_date = forms.DateField(label='Дата начала', widget=forms.SelectDateWidget)
    class Meta:
        model = Projects
        fields = ['name', 'description', 'status', 'users']
        profile_fields = ['users']

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop('pk')
        super().__init__(*args, **kwargs)
        self.fields['users'].queryset = User.objects.all().exclude(pk=pk)


class Team(forms.ModelForm):
    created_date = forms.DateField(label='Дата начала', widget=forms.SelectDateWidget)

    class Meta:
        model = Teams
        exclude = ['project', 'updated_date']

class TeamDelete(forms.ModelForm):
    class Meta:
        model = Teams
        fields=['user']

    # def clean_user(self):
    #     user = self.cleaned_data.get('user')
    #     user = User.objects.get(username=user)
    #     print(self.request.user)
    #     if self.request.user == user:
    #         raise ValidationError('Вы не можете удалить из проекта сами себя.', code='invalid_delete')
    #     else:
    #         return user
