from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,DeleteView

from accounts.models import Teams
from webapp.forms import Team, TeamDelete
from webapp.models import  Projects


class TeamsCreate(PermissionRequiredMixin,CreateView):
    template_name = 'teams/teams_form.html'
    model = Teams
    form_class = Team
    permission_required = 'webapp.add_teams'
    permission_denied_message = 'Доступ запрещен!'

    def form_valid(self, form):
        project = Projects.objects.get(id=self.request.path.split('/')[-1])
        Teams.objects.create(
            user=form.cleaned_data['user'],
            project=project,
            created_date=form.cleaned_data['created_date']
        )
        print(form.cleaned_data['user'])
        return redirect('projects_view', project.id)

    def get_form(self, form_class=None):
        form = super(TeamsCreate,self).get_form()
        project = Projects.objects.get(id=self.request.path.split('/')[-1])
        teams = Teams.objects.filter(project=project)
        closed_users = set()
        for i in teams:
            closed_users.add(i.user)
        form.fields['user'].queryset = User.objects.exclude(username__in=closed_users)
        return form

class TeamsDelete(PermissionRequiredMixin,CreateView):
    template_name = 'teams/teams_form.html'
    model = Teams
    form_class = TeamDelete
    permission_required = 'webapp.change_teams'
    permission_denied_message = 'Доступ запрещен!'

    def get_form(self, form_class=None):
        form = super(TeamsDelete,self).get_form()
        project = Projects.objects.get(id=self.request.path.split('/')[-1])
        teams = Teams.objects.filter(project=project).filter(updated_date__isnull=True)
        cur_users = set()
        for i in teams:
            cur_users.add(i.user)
        form.fields['user'].queryset = User.objects.filter(username__in=cur_users)
        return form

    def form_valid(self, form):
        project = Projects.objects.get(id=self.request.path.split('/')[-1])
        if form.cleaned_data['user'] == self.request.user:
            raise ValidationError('Вы не можете удалить из проекта сами себя.', code='invalid_delete')
        else:
            Teams.objects.filter(user=form.cleaned_data['user'], project=project).update(updated_date=datetime.now())
            return redirect('projects_view', project.id)