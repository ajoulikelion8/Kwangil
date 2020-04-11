from django.db import models
from myapp.models import Lion
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    name = models.ForeignKey (Lion, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField(max_length = 200)
    create_data = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return str(self.title)