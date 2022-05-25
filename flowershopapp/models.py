from django.db import models


class District(models.Model):
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Flower(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=250)
    customer_phone = models.CharField(max_length=12)
    customer_email = models.CharField(max_length=255)
    customer_address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
