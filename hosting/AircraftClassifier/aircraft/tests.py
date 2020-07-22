from django.test import TestCase
from aircraft.classifier.VariantClassifier import VariantClassifier
from PIL import Image
import os
import io

MODEL_PATH = path = os.path.join(os.getcwd(), 'classifier', 'trained_model')

TEST_IMG_PATH = 'test-image.jpg'
TEST_IMG_PATH_2 = 'test-image-2.jpg'


# Create your tests here.
def test_create_variant_classifier():
    VariantClassifier(MODEL_PATH)


def test_predict_variant_classifier():
    classifier = VariantClassifier(MODEL_PATH)
    with open(TEST_IMG_PATH, "rb") as f:
        result = classifier.predict(f.read())
        assert len(result) == VariantClassifier.class_count()


# Tests prediction on different images, checks that the images return different results.
def test_predict_diff_images():
    classifier = VariantClassifier(MODEL_PATH)
    with open(TEST_IMG_PATH, "rb") as f:
        result = classifier.predict(f.read())
        assert len(result) == VariantClassifier.class_count()

        with open(TEST_IMG_PATH_2, "rb") as f2:
            result2 = classifier.predict(f2.read())
            assert len(result2) == VariantClassifier.class_count()
            assert not (result is result2)
            assert result != result2
