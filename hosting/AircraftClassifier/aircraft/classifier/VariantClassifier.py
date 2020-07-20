import os
from tensorflow import keras
import PIL
import io
import tensorflow as tf
import numpy

# The image dimensions that the model was trained on.
IMG_HEIGHT = 244
IMG_WIDTH = 244

# Each pixel during training (and therefore during prediction) is rescaled from range [0, 255] to [0, 1].
PIXEL_RESCALE = 1./255

# The variant categories.
TEST_CLASSES = ["707-320", "737-800", "777-200", "a330-200", "bae 146-300", "c-130", "eurofighter typhoon", "md-80", "spitfire"]


class VariantClassifier:
    def __init__(self, model_path):
        self.model = keras.models.load_model(model_path)

    @staticmethod
    def class_count():
        return len(TEST_CLASSES)

    @classmethod
    def load_image(cls, b):
        return tf.image.decode_image(b, channels=3, dtype=tf.dtypes.float32)

    @classmethod
    def preprocess(cls, img):
        # resized = img.transform(size=(IMG_WIDTH, IMG_HEIGHT), method=PIL.Image.AFFINE)
        resized = tf.image.resize(img, [IMG_HEIGHT, IMG_WIDTH])
        normalised = resized * PIXEL_RESCALE

        return normalised

    def predict(self, img):
        image = self.load_image(img)
        preprocessed = self.preprocess(image)

        # Adds the batch column (with a value of 1 as this is a single image)
        batched = tf.expand_dims(preprocessed, 0)

        tf.ensure_shape(batched, (None, 244, 244, 3))

        predictions = self.model.predict(batched)[0]

        predictions = (predictions / numpy.sum(predictions))

        formatted = []

        for i, percentage in enumerate(predictions):
            formatted.append({
                'variant_name': TEST_CLASSES[i],
                'probability': percentage
            })

        return formatted
