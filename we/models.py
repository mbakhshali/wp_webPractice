from django.db import models

# Create your models here.

class ReportModel(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=11)
