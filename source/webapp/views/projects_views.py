# Create your views here.
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from accounts.models import Teams
from webapp.forms import SimpleSearchForm, UserToProject
from webapp.models import Projects
from webapp.views.base_views import SearchView


class ProjectsList(SearchView):
    template_name = 'projects/projects_list.html'
    model = Projects
    form = SimpleSearchForm

    def get_query(self):
        return Q(name__icontains=self.search_value)



class ProjectsDetail(DetailView):
    template_name = 'projects/projects_detail.html'
    model = Projects
    context_key = 'object'

    def get_context_data(self, **kwargs):
        context = super(ProjectsDetail,self).get_context_data(**kwargs)
        project = Projects.objects.get(id=self.request.path.split('/')[-1])
        context['users'] = Teams.objects.filter(project=project).exclude(updated_date__isnull=False)
        return context


class ProjectsCreate(PermissionRequiredMixin,CreateView):
    template_name = 'projects/projects_form.html'
    model = Projects
    success_url = reverse_lazy('projects_list')
    form_class = UserToProject
    permission_required = 'webapp.add_projects'
    permission_denied_message = 'Доступ запрещен'

    def form_valid(self, form):
        self.object = form.save()
        print(User.objects.get(id=self.request.user.id))
        Teams.objects.create(
            user=User.objects.get(id=self.request.user.id),
            project=self.object,
            created_date=datetime.now()
        )
        for i in form.cleaned_data['users']:
            print(User.objects.get(username=i))
            Teams.objects.create(
                user=User.objects.get(username=i),
                project=self.object,
                created_date=form.cleaned_data['start_date']
            )
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['pk'] = self.request.user.id
        return kwargs


class ProjectsUpdate(PermissionRequiredMixin,UpdateView):
    template_name = 'projects/projects_update.html'
    model = Projects
    fields = ['name', 'description', 'status']
    success_url = reverse_lazy('projects_list')
    permission_required = 'webapp.change_projects'
    permission_denied_message = 'Доступ запрещен'


class ProjectsDelete(PermissionRequiredMixin,DeleteView):
    template_name = 'projects/projects_delete.html'
    model = Projects
    success_url = reverse_lazy('projects_list')
    permission_required = 'webapp.delete_projects'
    permission_denied_message = 'Доступ запрещен'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.status = 'closed'
        self.object.save()
        return HttpResponseRedirect(success_url)