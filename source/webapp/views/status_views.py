from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from webapp.models import Statuses


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
