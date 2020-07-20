from django.test import TestCase
from aircraft.classifier.VariantClassifier import VariantClassifier
from PIL import Image
import os
import io

MODEL_PATH = path = os.path.join(os.getcwd(), 'classifier', 'trained_model')

TEST_IMG_PATH = 'test-image.jpg'


# Create your tests here.
def test_create_variant_classifier():
    VariantClassifier(MODEL_PATH)


def test_predict_variant_classifier():
    classifier = VariantClassifier(MODEL_PATH)
    with open(TEST_IMG_PATH, "rb") as f:
        result = classifier.predict(f.read())
        assert len(result) == VariantClassifier.class_count()
