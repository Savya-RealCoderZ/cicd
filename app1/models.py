from django.db import models

class cars(models.Model):
    carID = models.CharField(max_length=10)
    carName = models.CharField(max_length=10)