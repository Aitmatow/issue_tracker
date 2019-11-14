
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from accounts.models import Teams
from webapp.forms import Team
from webapp.models import Tips, Projects


class TeamsList(ListView):
    template_name = 'teams/teams_list.html'
    model = Teams
    paginate_by = 5
    paginate_orphans = 1
    page_kwarg = 'page'


class TeamsDetail(DetailView):
    template_name = 'teams/teams_detail.html'
    model = Teams

class TeamsCreate(LoginRequiredMixin,CreateView):
    template_name = 'teams/teams_form.html'
    model = Teams
    success_url = reverse_lazy('projects_list')
    form_class = Team

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


class TeamsUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'teams/teams_form.html'
    model = Teams
    success_url = reverse_lazy('teams_list')
    form_class = Team

class TeamsDelete(LoginRequiredMixin,DeleteView):
    template_name = 'teams/teams_delete.html'
    model = Teams
    success_url = reverse_lazy('teams_list')