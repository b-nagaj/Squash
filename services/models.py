from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.FileField(upload_to="service_logos/", blank=True)