from django.db import models


# Create your models here.
class DeriveHome(models.Model):
    image = models.CharField(max_length=100)
    image_file = models.ImageField(upload_to='deriveweb/static/img')


class DeriveBeer(models.Model):
    beer = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=100)
    image_file = models.ImageField(upload_to='deriveweb/static/img')
