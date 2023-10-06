from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    category = models.CharField(max_length=50)
