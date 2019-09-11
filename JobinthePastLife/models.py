from django.db import models

class PastLife(models.Model):
    name = models.CharField(max_length=4)
    job = models.CharField(max_length=20)
    birthday = models.CharField(max_length=15)