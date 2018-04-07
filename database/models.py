from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Charity(models.Model):
    name = models.CharField(max_length=40)
    lat = models.DecimalField(max_digits=13, decimal_places=10)
    lng = models.DecimalField(max_digits=13, decimal_places=10)
    needs = ArrayField(
        models.CharField(max_length=15)
    )
    #priorities = ArrayField(
    #        best

    class Meta:
        verbose_name = "Charity"
        verbose_name_plural = "Charities"

    def __str__(self):
        return self.name
