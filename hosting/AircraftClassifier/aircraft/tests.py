from django.test import TestCase
from aircraft.classifier.VariantClassifier import VariantClassifier
from PIL import Image

# Create your tests here.
def test_create_VariantClassifier():
    VariantClassifier()

def test_predict_VariantClassifier():
    classifier = VariantClassifier()
    img = Image.open("test-image.jpg")

    classifier.predict(img)
