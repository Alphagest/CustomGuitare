from django.db import models


class Article(models.Model):
    titre = models.CharField(max_length=400)
    description = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
