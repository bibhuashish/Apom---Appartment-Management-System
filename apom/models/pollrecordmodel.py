from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from apom.models.pollmodel import Poll


class Pollrecord(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.BooleanField(null=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

