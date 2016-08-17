from django.db import models

class Making(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)