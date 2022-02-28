from django.db import models

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200, null = True, blank = True)
    def __str__(self):
        return self.name

class Room(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, default='images.jpg')
    updated = models.DateTimeField(auto_now= True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title