# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from webapp.forms import IssueForm
from webapp.models import Issue

from .base_views import UpdateView, DetailView, DeleteView


class IssueList(ListView):
    template_name = 'issue/issue_list.html'
    model = Issue
    paginate_by = 4
    paginate_orphans = 1
    page_kwarg = 'page'

class IssueDetail(DetailView):
    template_name = 'issue/issue_detail.html'
    model = Issue
    context_key = 'object'


class IssueCreate(CreateView):
    template_name = 'issue/issue_form.html'
    model = Issue
    fields = ['title', 'description', 'status', 'tip']
    success_url = reverse_lazy('issue_list')


class IssueUpdate(UpdateView):
    # template_name = 'issue/issue_form.html'
    # model = Issue
    # fields = ['title', 'description', 'status', 'tip']
    # success_url = reverse_lazy('issue_list')

    form_class = IssueForm
    template_name = 'issue/issue_form.html'
    model = Issue
    redirect_url = 'issue_list'

class IssueDelete(DeleteView):
    template_name = 'issue/issue_delete.html'
    model = Issue
    redirect_url = 'issue_list'
    confirmation_for_delete = False
