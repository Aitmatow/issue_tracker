# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from webapp.forms import SimpleSearchForm
from webapp.models import Projects
from webapp.views.base_views import SearchView


class ProjectsList(SearchView):
    template_name = 'projects/projects_list.html'
    model = Projects
    form = SimpleSearchForm
    searched_fields = ['name']

class ProjectsDetail(DetailView):
    template_name = 'projects/projects_detail.html'
    model = Projects
    context_key = 'object'


class ProjectsCreate(CreateView):
    template_name = 'projects/projects_form.html'
    model = Projects
    fields = ['name', 'description', 'status']
    success_url = reverse_lazy('projects_list')


class ProjectsUpdate(UpdateView):
    template_name = 'projects/projects_form.html'
    model = Projects
    fields = ['name', 'description', 'status']
    success_url = reverse_lazy('projects_list')


class ProjectsDelete(DeleteView):
    template_name = 'projects/projects_delete.html'
    model = Projects
    success_url = reverse_lazy('projects_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.status = 'closed'
        self.object.save()
        return HttpResponseRedirect(success_url)