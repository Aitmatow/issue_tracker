
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
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
        """If the form is valid, save the associated model."""
        # self.object = form.save()
        project = Projects.objects.get(id=self.request.path.split('/')[-1])
        Teams.objects.create(
            user=form.cleaned_data['user'],
            project=project,
            created_date=form.cleaned_data['created_date']
        )
        return redirect('projects_view', project.id)


class TeamsUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'teams/teams_form.html'
    model = Teams
    # fields = ['user', 'project', 'created_date', 'updated_date']
    success_url = reverse_lazy('teams_list')
    form_class = Team

class TeamsDelete(LoginRequiredMixin,DeleteView):
    template_name = 'teams/teams_delete.html'
    model = Teams
    success_url = reverse_lazy('teams_list')