from django.db import models

# Create your models here.

# Defining Event model
class Example(models.Model):
    name = models.TextField(blank=True)
    url = models.URLField()