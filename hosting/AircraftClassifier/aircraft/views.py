from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

from django.views.decorators.csrf import csrf_exempt

import time
import json


# Create your views here.
def predict_image(request):
    context = {}
    return render(request, 'aircraft/predict.html', context)

# TODO, sort csrf.
@csrf_exempt
def predict_aircraft_variant(request):
    # if request.method == 'POST':
    #    form = ImageFileUploadForm(request.POST, request.FILES)
    #    if form.is_valid():
    #        form.save()
    #        return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
    #    else:
    #        return JsonResponse({'error': True, 'errors': form.errors})
    # else:
    #     form = ImageFileUploadForm()
    #     return render(request, 'django_image_upload_ajax.html', {'form': form})
    print("Predict aircraft variant called")
    with open('temp.jpg', 'wb') as temp:
        for chunk in request.FILES['file1'].chunks():
            temp.write(chunk)

    # attached_file1 = files.get('file1', None)
    # # form = FileUploadForm(data=request.POST, files=request.FILES)
    # # data = request.FileField()
    # # data = json.loads(request.body)
    # # files = request.FILEs
    # # file = files.get('file', None)
    # # attr1 = data.get('attr1')
    # # print(attached_file1)
    # with open('temp.jpg', 'wb') as f:
    #     f.write(file)
    # time.sleep(2.0)
    return HttpResponse(status=501, reason="Predict API not implemented")
