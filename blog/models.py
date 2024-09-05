from django.db import models
from django.utils import timezone
from django import forms
from ckeditor.fields import RichTextField
import datetime


class Tour(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=100, blank=True)
    description = models.TextField(default="")
    route = RichTextField(default="")  # Formatowalny tekst "Что вас ожидает"
    price = models.DecimalField(max_digits=10, decimal_places=2)
    departure_date = models.DateField(default=timezone.now)  # Możesz usunąć, jeśli to zbędne
    duration = models.IntegerField(default=1)
    starting_point = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='tours/')
    organizational_details = RichTextField(blank=True, null=True)  # Szczegóły organizacyjne
    available_dates = models.JSONField(default=list, blank=True)  # Jeśli później będziesz integrować z kalendarzem

    def __str__(self):
        return self.title

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['title', 'short_description']
        widgets = {
            'short_description': forms.TextInput(attrs={'maxlength': '100'}),
        }

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
