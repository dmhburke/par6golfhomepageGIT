from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import Sum, Count
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class TourModel(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    tour_number = models.IntegerField(blank=True, null=True)
    tour_dates = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class PlayerModel(models.Model):
     name = models.CharField(max_length=30)
     image = models.ImageField(upload_to='playerimages', blank=True, null=True)

     def __str__(self):
         return self.name

class TourPlayerModel(models.Model):
    tour_title = models.ForeignKey('TourModel',on_delete = models.CASCADE, blank=True, null=True)
    tour_player = models.ForeignKey('PlayerModel',on_delete = models.CASCADE, blank=True, null=True)
    tour_points = models.IntegerField(blank=True, null=True)
    tour_position = models.IntegerField(blank=True, null=True)
    tour_organizer = models.CharField(max_length=30, blank=True, null=True)

class TourCoursesModel(models.Model):
    tour_title = models.ForeignKey('TourModel',on_delete = models.CASCADE, blank=True, null=True)
    tour_course = models.CharField(max_length=50, blank=True, null=True)


# NEXT STEPS: ADD TourCourses Model and include results in TourPlayer Model
