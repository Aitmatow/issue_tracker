
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import  ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from webapp.models import Statuses

from webapp.views.base_views import DetailView

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
