from django.contrib.auth.models import User
from django.db import models

class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, null=False)
    community = models.CharField(max_length=100, null=False)
    block = models.CharField(max_length=100)
    home = models.CharField(max_length=100, null=False)




