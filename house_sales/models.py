from django.db import models
from location_field.models.plain import PlainLocationField
from django.utils.timesince import timesince
from django.utils import timezone

class SellHouses(models.Model):
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

class SellVilla(SellHouses):
    pass

class SellGroundPlus(SellHouses):
    pass

class SellBuildings(SellHouses):
    pass

class SellAppartment(SellHouses):
    pass

class SellCondominum(SellHouses):
    pass

class SellStudio(SellHouses):
    pass
