from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=180)

    def __str__(self):
        return self.name