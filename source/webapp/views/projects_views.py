# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from webapp.models import Projects



class ProjectsList(ListView):
    template_name = 'projects/projects_list.html'
    model = Projects
    paginate_by = 4
    paginate_orphans = 1
    page_kwarg = 'page'

class ProjectsDetail(DetailView):
    template_name = 'projects/projects_detail.html'
    model = Projects
    context_key = 'object'


class ProjectsCreate(CreateView):
    template_name = 'projects/projects_form.html'
    model = Projects
    fields = ['name', 'description']
    success_url = reverse_lazy('projects_list')


class ProjectsUpdate(UpdateView):
    template_name = 'projects/projects_form.html'
    model = Projects
    fields = ['name', 'description']
    success_url = reverse_lazy('projects_list')


class ProjectsDelete(DeleteView):
    template_name = 'projects/projects_delete.html'
    model = Projects
    success_url = reverse_lazy('projects_list')