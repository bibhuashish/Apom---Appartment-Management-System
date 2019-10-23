from django.conf import settings
from django.db import models

class Resident(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, null=False)
    community = models.CharField(max_length=100, null=False)
    block = models.CharField(max_length=100)
    home = models.CharField(max_length=100, null=False)




