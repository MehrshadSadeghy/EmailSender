from django.db import models


class Information(models.Model):
    to_email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=255, blank=True, null=True)
    information = models.TextField(blank=True, null=True)
