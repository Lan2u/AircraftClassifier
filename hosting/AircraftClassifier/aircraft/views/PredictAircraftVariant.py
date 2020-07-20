# Used for the predict aircraft variant API.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic import TemplateView

from aircraft.classifier.VariantClassifier import VariantClassifier


class PredictAircraftVariant(TemplateView):
    ENDPOINT = 'predict/aircraft/variant/'

    template_name = 'aircraft/api.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.classifier = VariantClassifier()


    @csrf_exempt
    def post(self, request):
        print("Predict aircraft variant called")
        img = request.FILES['predictFile'].read()
        self.classifier.predict(img)

        # with open('temp.jpg', 'wb') as temp:
        #     for chunk in request.FILES['predictFile'].chunks():
        #         temp.write(chunk)
        return HttpResponse(status=501, reason="Predict API not implemented")
