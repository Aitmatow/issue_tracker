
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from webapp.forms import StatusForm
from webapp.models import Statuses


class StatusList(ListView):
    template_name = 'status/statuses_list.html'
    model = Statuses
    paginate_by = 5
    paginate_orphans = 1
    page_kwarg = 'page'

class StatusDetail(DetailView):
    template_name = 'status/statuses_detail.html'
    model = Statuses
    context_key = 'object'

class StatusCreate(LoginRequiredMixin,CreateView):
    template_name = 'status/statuses_form.html'
    model = Statuses
    fields = ['name']
    success_url = reverse_lazy('status_list')

class StatusUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'status/statuses_form.html'
    model = Statuses
    fields = ['name']
    success_url = reverse_lazy('status_list')

class StatusDelete(LoginRequiredMixin,DeleteView):
    template_name = 'status/statuses_delete.html'
    model = Statuses
    success_url = reverse_lazy('status_list')
