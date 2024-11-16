from django.db import models  # type: ignore

# Create your models here.

class CarouselImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carousel_images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title