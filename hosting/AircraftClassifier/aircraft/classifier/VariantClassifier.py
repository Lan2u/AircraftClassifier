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
    def __init__(self):
        # model_path = os.path.join(os.getcwd(), 'aircraft', 'classifier', 'trained_model')
        model_path = os.path.join(os.getcwd(), 'classifier', 'trained_model')
        self.model = keras.models.load_model(model_path)

    def load_image(self, bytes):
        # image = PIL.Image.frombytes()
        # data = io.BytesIO(bytes)
        # return PIL.Image.open(data)
        # image.show()
        return tf.image.decode_image(bytes, channels=3, dtype=tf.dtypes.float32)

    def preprocess(self, img):
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

        for i, percentage in enumerate(predictions):
            predictions[i] = {
                'variant_name': TEST_CLASSES[i],
                'probability': percentage
            }

        return predictions
