from django.views.generic import TemplateView, FormView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import RequetForm

class IndexView(TemplateView):
    template_name = "index.html"

class RequestView(FormView):
    template_name = "request.html"
    form_class = RequetForm
    success_url = reverse_lazy('main_page:request')

    def form_valid(self, form):

        request_result = ""
        print(type(form))

        for key, value in form.cleaned_data.items():
            request_result = request_result + value
            context = {
                'result': request_result,
                'form': form
            }

        if 'generate' in self.request.POST:
            return render(self.request, 'request.html', context)

