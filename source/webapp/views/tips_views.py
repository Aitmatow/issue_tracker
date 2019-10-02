from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from webapp.models import Statuses, Tips

from webapp.forms import IssueForm
from webapp.models import Issue


class IndexView(TemplateView):
    template_name = 'issue/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context


class IssueView(TemplateView):
    template_name = 'issue/issue.html'
    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=pk)
        return context

class IssueCreate(View):
    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, 'issue/create.html', context={
            'form' : form
        })

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                tip=form.cleaned_data['tip']
            )
            return redirect('issue_view', pk = issue.pk)
        else:
            return render(request, 'issue/create.html', context={
                'form' : form
            })


class IssueUpdate(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(data={
            'title': issue.title,
            'description':issue.description,
            'status':issue.status_id,
            'tip':issue.tip_id
        })
        return render(request, 'issue/update.html', context={
            'form' : form,
            'issue' : issue
        })

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue.title=form.cleaned_data['title']
            issue.description=form.cleaned_data['description']
            issue.status=form.cleaned_data['status']
            issue.tip=form.cleaned_data['tip']
            issue.save()
            return redirect('issue_view', pk = issue.pk)
        else:
            return render(request, 'issue/update.html', context={
                'form' : form,
                'issue' : issue
            })

class IssueDelete(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        return render(request, 'issue/delete.html', context={'issue':issue})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        issue.delete()
        return redirect('index')

class StatusList(ListView):
    template_name = 'status/statuses_list.html'
    model = Statuses

class StatusDetail(DetailView):
    template_name = 'status/statuses_detail.html'
    model = Statuses

class StatusCreate(CreateView):
    template_name = 'status/statuses_form.html'
    model = Statuses
    fields = ['name']
    success_url = reverse_lazy('status_list')

class StatusUpdate(UpdateView):
    template_name = 'status/statuses_form.html'
    model = Statuses
    fields = ['name']
    success_url = reverse_lazy('status_list')

class StatusDelete(DeleteView):
    template_name = 'status/statuses_delete.html'
    model = Statuses
    success_url = reverse_lazy('status_list')


class TipsList(ListView):
    template_name = 'tips/tips_list.html'
    model = Tips

class TipsDetail(DetailView):
    template_name = 'tips/tips_detail.html'
    model = Tips

class TipsCreate(CreateView):
    template_name = 'tips/tips_form.html'
    model = Tips
    fields = ['name']
    success_url = reverse_lazy('tips_list')

class TipsUpdate(UpdateView):
    template_name = 'tips/tips_form.html'
    model = Tips
    fields = ['name']
    success_url = reverse_lazy('tips_list')

class TipsDelete(DeleteView):
    template_name = 'tips/tips_delete.html'
    model = Tips
    success_url = reverse_lazy('tips_list')