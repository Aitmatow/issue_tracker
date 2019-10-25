# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.http import urlencode

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from webapp.forms import SimpleSearchForm
from webapp.models import Issue



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


class IssueCreate(LoginRequiredMixin, CreateView):
    template_name = 'issue/issue_form.html'
    model = Issue
    fields = ['title', 'description', 'project', 'status', 'tip']
    success_url = reverse_lazy('issue_list')


class IssueUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'issue/issue_form.html'
    model = Issue
    fields = ['title', 'description', 'project', 'status', 'tip']
    success_url = reverse_lazy('issue_list')


class IssueDelete(LoginRequiredMixin,DeleteView):
    template_name = 'issue/issue_delete.html'
    model = Issue
    success_url = reverse_lazy('issue_list')