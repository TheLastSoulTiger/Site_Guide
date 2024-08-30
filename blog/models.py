from django.db import models
from django.utils import timezone
import datetime


class Tour(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField(default="")
    description = models.TextField()
    route = models.TextField(default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    departure_date = models.DateField(default=timezone.now)
    duration = models.IntegerField(default=1)
    starting_point = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='tours/')
    # images = models.ImageField(upload_to='tour_images/', blank=True, null=True)


    def __str__(self):
        return self.title


class TourImage(models.Model):
    image = models.ImageField(upload_to='tour_images/')
    tour = models.ForeignKey(Tour, related_name='tour_images', on_delete=models.CASCADE)  # Added related_name

    def __str__(self):
        return f"Image for {self.tour.title}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    tour = models.ForeignKey(Tour, related_name='reviews', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.tour.title}'
