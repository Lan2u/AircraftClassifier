# Used for the predict aircraft variant API.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import TemplateView

import os

from aircraft.classifier.VariantClassifier import VariantClassifier

MODEL_PATH = os.path.join(os.getcwd(), 'aircraft', 'classifier', 'trained_model')

class PredictAircraftVariant(TemplateView):
    ENDPOINT = 'predict/aircraft/variant/'

    template_name = 'aircraft/api.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.classifier = VariantClassifier(MODEL_PATH)


    @csrf_exempt
    def post(self, request):
        print("Predict aircraft variant called")
        img = request.FILES['predictFile'].read()
        res = self.classifier.predict(img)
        print(res)

        result = {
            'file-name': request.FILES['predictFile'].name(),
            'predictions': res
        }

        # with open('temp.jpg', 'wb') as temp:
        #     for chunk in request.FILES['predictFile'].chunks():
        #         temp.write(chunk)
        return JsonResponse(result)
