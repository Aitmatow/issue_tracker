from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import IssueForm
from webapp.models import Issue


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context


class IssueView(TemplateView):
    template_name = 'issue.html'
    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=pk)
        return context

class IssueCreate(View):
    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, 'create.html',context={
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
            return render(request, 'create.html', context={
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
        return render(request, 'update.html',context={
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
            return render(request, 'update.html', context={
                'form' : form,
                'issue' : issue
            })
