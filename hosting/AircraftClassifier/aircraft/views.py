from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.views.decorators.csrf import csrf_exempt

import time


# Create your views here.
def predict_image(request):
    template = loader.get_template('aircraft/predict.html')
    context = {}
    return render(request, 'aircraft/predict.html', context)


# TODO, sort csrf.
@csrf_exempt
def predict_aircraft_variant(request):
    print("Predict aircraft variant called")
    time.sleep(2.0)
    return HttpResponse(status=501, reason="Predict API not implemented")
