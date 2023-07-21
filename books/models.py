from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')  # 'images/' is the folder where images will be stored
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
