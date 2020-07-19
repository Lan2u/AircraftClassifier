from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def predict_image(request):
    context = {}
    return render(request, 'aircraft/predict.html', context)

# TODO, sort csrf.
@csrf_exempt
def predict_aircraft_variant(request):
    print("Predict aircraft variant called")
    with open('temp.jpg', 'wb') as temp:
        for chunk in request.FILES['predictFile'].chunks():
            temp.write(chunk)
    return HttpResponse(status=501, reason="Predict API not implemented")
