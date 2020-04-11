from django.db import models
from django.utils import timezone

# Create your models here.

class Lion(models.Model):
    name = models.CharField(max_length = 100)
    create_data = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return str(self.name)