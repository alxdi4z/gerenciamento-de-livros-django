from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=180)
    author = models.CharField(max_length=180)
    isbn = models.IntegerField(max_length=13)
    
