from django import forms
from django.forms import widgets
from webapp.models import Issue, Statuses, Tips

class IssueForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label = 'Наименование')
    description = forms.CharField(max_length=3000, required=False, label='Описание', widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Statuses.objects.all(), label='Статус', required=True, empty_label=None)
    tip = forms.ModelChoiceField(queryset=Tips.objects.all(), label='Тип задачи', required=True, empty_label=None)
