from django.contrib import admin # type: ignore

# Register your models here.
from .models import CarouselImage

admin.site.register(CarouselImage)