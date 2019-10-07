
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import  ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from webapp.forms import TipsForm
from webapp.models import  Tips
from .base_views import UpdateView, DetailView, DeleteView

class TipsList(ListView):
    template_name = 'tips/tips_list.html'
    model = Tips
    paginate_by = 5
    paginate_orphans = 1
    page_kwarg = 'page'


class TipsDetail(DetailView):
    template_name = 'tips/tips_detail.html'
    model = Tips
    context_key = 'object'

class TipsCreate(CreateView):
    template_name = 'tips/tips_form.html'
    model = Tips
    fields = ['name']
    success_url = reverse_lazy('tips_list')

class TipsUpdate(UpdateView):
    # template_name = 'tips/tips_form.html'
    # model = Tips
    # fields = ['name']
    # success_url = reverse_lazy('tips_list')

    form_class = TipsForm
    template_name = 'tips/tips_form.html'
    model = Tips
    redirect_url = 'tips_list'

class TipsDelete(DeleteView):
    template_name = 'tips/tips_delete.html'
    model = Tips
    redirect_url = 'tips_list'
    confirmation_for_delete = False