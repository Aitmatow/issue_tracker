from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class DetailView(TemplateView):
    context_key = 'objects'
    model = None

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context[self.context_key] = get_object_or_404(self.model, pk=pk)
        return context

    def get_objects(self):
        return self.model.objects.all()