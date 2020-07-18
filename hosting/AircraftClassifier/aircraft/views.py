from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def predict_image(request):
    template = loader.get_template('aircraft/predict.html')
    context = {}
    return render(request, 'aircraft/predict.html', context)