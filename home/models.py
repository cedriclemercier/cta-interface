# models.py
from django.db import models

class Image(models.Model):
    file = models.ImageField(
        null=False,
        blank=False
        # upload_to='images/'
        )