from django.db import models

# Create your models here.
class Container(models.Model):
    container_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.container_id