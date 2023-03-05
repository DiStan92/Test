from django.db import models

class Article(models.Model):
    article = models.IntegerField()
    brand = models.CharField(max_length=250)
    title = models.CharField(max_length=250)

