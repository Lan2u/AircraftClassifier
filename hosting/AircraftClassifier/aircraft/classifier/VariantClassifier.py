import os
from tensorflow import keras
import PIL
import io


class VariantClassifier:
    def __init__(self):
        model_path = os.path.join(os.getcwd(), 'aircraft', 'classifier', 'trained_model')
        self.model = keras.models.load_model(model_path)

    def load_image(self, bytes):
        # image = PIL.Image.frombytes()
        data = io.BytesIO(bytes)
        return PIL.Image.open(data)
        # image.show()

    def preprocess(self, img):
        return img

    def predict(self, img):
        image = self.load_image(img)
        return self.model.predict(self.preprocess(image))