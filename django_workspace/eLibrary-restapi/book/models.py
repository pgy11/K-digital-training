from django.db import models

# Create your models here.
class Book(models.Model):
    image_URL = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    edition = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200, primary_key=True, null=False, blank=False)
    rating = models.FloatField()
    objects = models.Manager()