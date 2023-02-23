from django.db import models


# Create your models here.
class Consultation(models.Model):
    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=64)

class Question(models.Model):
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=64)
    question = models.CharField(max_length=200)

class PriceInfo(models.Model):
    priceName = models.CharField(max_length=200)
    priceDescrip = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=64)

class Image(models.Model):
    nameImg = models.CharField(max_length=32)
    image=models.ImageField(upload_to="media")