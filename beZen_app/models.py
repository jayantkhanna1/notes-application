from datetime import datetime
from django.db import models

# Create your models here.
class Note(models.Model):
    heading = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField()
    lastUpdated = models.DateTimeField()
    important = models.BooleanField(default=False)
