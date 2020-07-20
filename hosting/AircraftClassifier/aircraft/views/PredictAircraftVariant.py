# Used for the predict aircraft variant API.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import TemplateView

import os
import json

from aircraft.classifier.VariantClassifier import VariantClassifier

MODEL_PATH = os.path.join(os.getcwd(), 'aircraft', 'classifier', 'trained_model')


class PredictAircraftVariant(TemplateView):
    ENDPOINT = 'predict/aircraft/variant/'

    template_name = 'aircraft/api.html'

    # Statically loaded as otherwise each request needs to reload the model which takes too long.
    classifier = VariantClassifier(MODEL_PATH)

    def post(self, request):
        img = request.FILES['predictFile'].read()
        res = PredictAircraftVariant.classifier.predict(img)

        stringify = []
        for r in res:
            stringify.append({
                'variant_name': r['variant_name'],
                'probability': str(r['probability'])
            })

        result = {
            'file-name': str(request.FILES['predictFile']),
            'predictions': json.dumps(stringify)
        }

        # with open('temp.jpg', 'wb') as temp:
        #     for chunk in request.FILES['predictFile'].chunks():
        #         temp.write(chunk)
        return JsonResponse(result)
