from django.db import models


class Container(models.Model):
    container_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.container_id
    

class ContainerImage(models.Model):
    image = models.FileField(storage='containertrack_api.storage_backend.SupabaseStorage')
    container = models.ForeignKey(Container, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image