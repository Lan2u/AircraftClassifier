from django.db import models

# Create your models here.


# Represents an aircraft variant
class AircraftVariant(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


# Represents an aircraft image which may or may not have been classified.
class AircraftImage(models.Model):
    # An ID field is created automatically by django.
    path = models.FilePathField('Image Path')
    predicted_variant = AircraftVariant()
    actual_variant = AircraftVariant()
    image_name = models.CharField(max_length=256)

    def __str__(self):
        return self.image_name


