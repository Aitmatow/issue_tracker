from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import TemplateView

from webapp.models import Issue


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


class UpdateView(View):
    form_class = None
    template_name = None
    model = None
    redirect_url = None

    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(self.model, pk = kwargs.get('pk'))
        form = self.form_class(instance = issue)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(self.model, pk=kwargs.get('pk'))
        form = self.form_class(instance = issue, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        context = {'form': form}
        return render(self.request, self.template_name, context)

    def get_redirect_url(self):
        return self.redirect_url


class DeleteView(View):
    template_name = None
    model = None
    redirect_url = None
    confirmation_for_delete = None


    def get(self, request, *args, **kwargs):
        object = get_object_or_404(self.model, pk=kwargs.get('pk'))
        if self.confirmation_for_delete == True:
            context = {'object': object}
            return render(self.request, self.template_name, context)
        else:
            object.delete()
            return redirect(self.get_redirect_url())

    def post(self, request, *args, **kwargs):
        object = get_object_or_404(self.model, pk = kwargs.get('pk'))
        object.delete()
        return redirect(self.get_redirect_url())


    def get_redirect_url(self):
        return self.redirect_url