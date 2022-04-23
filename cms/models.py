from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    featured_image = models.ImageField(default='images/default.png', upload_to='images/')


    def __str__(self):
        return self.title