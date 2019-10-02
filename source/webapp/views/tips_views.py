from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from webapp.models import  Tips



class TipsList(ListView):
    template_name = 'tips/tips_list.html'
    model = Tips
    paginate_by = 5
    paginate_orphans = 1
    page_kwarg = 'page'


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