# The page where you can submit an image and get results from giving it to the model.
from django.shortcuts import render
from django.views.generic import TemplateView


class PredictImagePage(TemplateView):
    ENDPOINT = 'predict/'

    def get(self, request):
        context = {}
        return render(request, 'aircraft/predict.html', context)
