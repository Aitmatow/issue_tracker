from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from webapp.models import Issue


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context