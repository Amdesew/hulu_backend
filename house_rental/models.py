from django.db import models
from location_field.models.plain import PlainLocationField
from django.utils.timesince import timesince
from django.utils import timezone



class RentHouses(models.Model):
    image = models.ImageField(upload_to="uploads/")
    second_image = models.ImageField(upload_to="second_uploads/")
    third_image = models.ImageField(upload_to="uploads/")
    fourth_image = models.ImageField(upload_to="uploads/")
    details = models.CharField(max_length=100)
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    area_square = models.IntegerField()
    garage = models.IntegerField()
    description = models.CharField(max_length=300)
    built_year = models.DateField()
    location = PlainLocationField(based_fields=['city'], zoom=7)
    posted_time = models.DateTimeField(auto_now_add=True)
    
    @property
    def time_since_upload(self):
        return timesince(self.posted_time, timezone.now())

class Villa(RentHouses):
    pass

class GroundPlus(RentHouses):
    pass

class Buildings(RentHouses):
    pass

class Appartment(RentHouses):
    pass

class Condominum(RentHouses):
    pass

class Studio(RentHouses):
    pass
