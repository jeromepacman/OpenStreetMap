from django.db import models
from django.shortcuts import reverse
from osm_field.fields import LatitudeField, LongitudeField, OSMField


class MyOsm(models.Model):
    location=OSMField()
    email=models.EmailField(blank=True)
    phone=models.IntegerField(null=True, blank=True)
    location_lat=LatitudeField()
    location_lon=LongitudeField()

    def __str__(self):
        return self.location


class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    date=models.DateField(auto_now_add=True)
    center=models.ForeignKey(MyOsm, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name



