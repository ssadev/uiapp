from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class blogs(models.Model):
    content = models.TextField()
    thumbnail = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content