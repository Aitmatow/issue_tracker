# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from webapp.models import Issue


class IssueList(ListView):
    template_name = 'issue/issue_list.html'
    model = Issue

class IssueDetail(DetailView):
    template_name = 'issue/issue_detail.html'
    model = Issue

class IssueCreate(CreateView):
    template_name = 'issue/issue_form.html'
    model = Issue
    fields = ['title', 'description', 'status', 'tip']
    success_url = reverse_lazy('issue_list')

class IssueUpdate(UpdateView):
    template_name = 'issue/issue_form.html'
    model = Issue
    fields = ['title', 'description', 'status', 'tip']
    success_url = reverse_lazy('issue_list')

class IssueDelete(DeleteView):
    template_name = 'issue/issue_delete.html'
    model = Issue
    success_url = reverse_lazy('issue_list')
