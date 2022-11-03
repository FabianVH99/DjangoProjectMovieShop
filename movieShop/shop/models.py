from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.CharField(max_length=5000, null=True, blank=True)