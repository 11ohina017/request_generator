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

        request_result_first = ""
        request_result_second = ""
        request_length_flag = False

        # フォームの値を結合
        for key, value in form.cleaned_data.items():

            if key == "request_length":
                request_length_flag = True
            else:
                if request_length_flag== False:
                    request_result_first = request_result_first + value
                else:
                    request_result_second = request_result_second + value

        # 要求データ長の作成
        request_length = len(request_result_second)
        print(request_length)
        request_length_hex = format(request_length, '04x')
        form.fields['request_length'].initial = request_length_hex

        request_result = request_result_first + request_length_hex + request_result_second
        context = {
            'result': request_result,
            'form': form
        }

        if 'generate' in self.request.POST:
            return render(self.request, 'request.html', context)

