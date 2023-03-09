from django.db import models
from django.db.transaction import atomic  ################# bring all or non
from django.shortcuts import get_object_or_404, get_list_or_404  ######## bring one or do 404 or bring list or 404
from django import forms
from django.contrib.auth.models import User


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.CharField(null=False, max_length=50)
    age = models.IntegerField(null=False)
    user = models.OneToOneField(null=False, to=User, on_delete=models.CASCADE)

    class Meta:
        db_table = "person"

    def __str__(self):
        return f"name:{self.user.username}\n" \
               f"id:{self.id}"


class Car(models.Model):
    car_type = models.CharField(null=False, max_length=50)
    cost = models.IntegerField(null=False)
    year = models.PositiveIntegerField(null=False)
    car_plate = models.CharField(null=False, max_length=50)
    owner = models.ForeignKey(Person, on_delete=models.RESTRICT,
                              related_name="car_owner", null=True)
    renters = models.ManyToManyField(Person, through="Rent", null=True, blank=True,
                                     related_name="rented_cars")

    class Meta:

        db_table = "car"

    def __str__(self):
        return f"{self.id}" \
               f"Car: {self.car_type}\n" \
               f"car_id: {self.car_plate}\n" \
               f"{self.owner}\n" \
               f"cost: {self.cost}"


class Rent(models.Model):
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    client = models.ForeignKey(Person, on_delete=models.RESTRICT)

    class Meta:
        db_table = "rent"

    def __str__(self):
        return f"{self.car}\n" \
               f"{self.start_date}\n" \
               f"{self.end_date}\n" \
               f"{self.client}"


