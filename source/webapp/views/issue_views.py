# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.utils.http import urlencode

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from accounts.models import Teams
from webapp.forms import SimpleSearchForm, IssueForm
from webapp.models import Issue, Projects


class IssueList(ListView):
    template_name = 'issue/issue_list.html'
    model = Issue
    paginate_by = 4
    paginate_orphans = 1
    page_kwarg = 'page'


    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(data=self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(title__icontains=self.search_value )
                | Q(description__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search' : self.search_value})
        return context

class IssueDetail(DetailView):
    template_name = 'issue/issue_detail.html'
    model = Issue
    context_key = 'object'


def edit_permission_test(project, user):
    user_obj = User.objects.get(username=user)
    temp = Teams.objects.filter(project=project).values('user')
    for i in temp:
        if (i.get('user') == user_obj.pk):
            return True
        return False


class IssueCreate(LoginRequiredMixin, CreateView):
    template_name = 'issue/issue_form.html'
    model = Issue
    # fields = ['title', 'description', 'project', 'status', 'tip', 'created_by', 'assigned_to']
    success_url = reverse_lazy('issue_list')
    form_class = IssueForm

    def get_form(self, form_class=None):
        form = super(IssueCreate,self).get_form()
        form.fields['created_by'].queryset = User.objects.filter(username=self.request.user)
        form.fields['project'].queryset = Projects.objects.filter(teams__user=self.request.user)
        cur_project = Projects.objects.filter(teams__user=self.request.user)
        users_in_team = Teams.objects.filter(project=cur_project[0])
        wanted_users = set()
        for i in users_in_team:
            wanted_users.add(i.user)
        form.fields['assigned_to'].queryset=User.objects.filter(username__in=wanted_users)
        return form


    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        project = form.cleaned_data.get('project')
        temp = edit_permission_test(project, self.request.user)
        if temp == True:
            self.object = form.save()
            return super().form_valid(form)
        else:
            return HttpResponseForbidden('У вас нет доступа к данному проекту!')



class IssueUpdate(UserPassesTestMixin,UpdateView):
    template_name = 'issue/issue_form.html'
    model = Issue
    # fields = ['title', 'description', 'project', 'status', 'tip']
    success_url = reverse_lazy('issue_list')
    form_class = IssueForm

    def get_form(self, form_class=None):
        form = super(IssueUpdate,self).get_form()
        form.fields['created_by'].queryset = User.objects.filter(username=self.request.user)
        form.fields['project'].queryset = Projects.objects.filter(teams__user=self.request.user)
        cur_project = Projects.objects.filter(teams__user=self.request.user)
        users_in_team = Teams.objects.filter(project=cur_project[0])
        wanted_users = set()
        for i in users_in_team:
            wanted_users.add(i.user)
        form.fields['assigned_to'].queryset=User.objects.filter(username__in=wanted_users)
        return form

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        project = form.cleaned_data.get('project')
        temp = edit_permission_test(project, self.request.user)
        if temp == True:
            self.object = form.save()
            return super().form_valid(form)
        else:
            # return HttpResponse('У вас нет доступа к данному проекту!', status=403)
            return HttpResponseForbidden('У вас нет доступа к данному проекту!')

    def test_func(self):
        obj = self.get_object().project
        return edit_permission_test(obj, self.request.user)


class IssueDelete(UserPassesTestMixin,DeleteView):
    template_name = 'issue/issue_delete.html'
    model = Issue
    success_url = reverse_lazy('issue_list')

    def test_func(self):
        obj = self.get_object().project
        return edit_permission_test(obj, self.request.user)