from django.db import models
from datetime import datetime

# Create your models here.

class Mentor(models.Model):
    nama = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=200)
    tahun_exp = models.IntegerField(default=0)
    quotes = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Mentee(models.Model):
    nama = models.CharField(max_length=255)
    testimoni = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    img_url = models.CharField(max_length=255)
    date_post = models.DateTimeField(default=datetime.now)
    total_comment = models.IntegerField(default=0)

    def __str__(self):
        return self.title



