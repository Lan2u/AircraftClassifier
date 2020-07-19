# The
from django.shortcuts import render
from django.views.generic import TemplateView


class PredictImagePage(TemplateView):
    ENDPOINT = 'predict/'

    def get(self, request):
        context = {}
        return render(request, 'aircraft/predict.html', context)
