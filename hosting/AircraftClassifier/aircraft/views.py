from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def predict_image(request):
    return HttpResponse("Predict Image View")