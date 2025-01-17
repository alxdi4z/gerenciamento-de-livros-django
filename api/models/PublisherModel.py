from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    foundation = models.DateField()
    description = models.TextField(blank=True)
