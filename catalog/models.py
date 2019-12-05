from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import Sum, Count, Min
from django.core.validators import MaxValueValidator, MinValueValidator
from catalog.choices import *

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
    mgmt_committee = models.CharField(choices=YES_NO, max_length=30, blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    nationality = models.CharField(choices=NATIONALITIES, max_length=30, blank=True, null=True)
    tour_number = models.IntegerField(blank=True, null=True)
    high_finish = models.IntegerField(blank=True, null=True)

    @property
    def nationality_flag(self):
        flag = self.nationality
        def get_flag(flag):
            switch_options = {
            "Australian": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Flag_of_Australia_%28converted%29.svg/1200px-Flag_of_Australia_%28converted%29.svg.png",
            "American":"https://cdn.webshopapp.com/shops/94414/files/54958226/the-united-states-flag-vector-free-download.jpg",
            "British": "https://cdn.britannica.com/25/4825-004-C11466B0/Flag-United-Kingdom.jpg",
            "Canadian": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Flag_of_Canada_%28Pantone%29.svg",
            "New Zealand": "https://upload.wikimedia.org/wikipedia/commons/b/b7/NZ_flag_design_Silver_Fern_%28Black_%26_White%29_by_Alofi_Kanter.svg",
            "Swedish": "https://upload.wikimedia.org/wikipedia/en/4/4c/Flag_of_Sweden.svg"
            }
            return switch_options.get(flag, "Error")
        return get_flag(flag)

    @property
    def roman_numerals(self):
        number = self.tour_number
        def get_numerals(number):
            switch_options = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X"
            }
            return switch_options.get(number, self.tour_number)
        return get_numerals(number)

    @property
    def result_jacket(self):
        result = self.high_finish
        def id_jacket(result):
            switch_options = {
            1: "Jacket",
            }
            return switch_options.get(result, self.high_finish)
        return id_jacket(result)

    def __str__(self):
        return self.name

class TourPlayerModel(models.Model):
    tour_title = models.ForeignKey('TourModel',on_delete = models.CASCADE, blank=True, null=True)
    tour_player = models.ForeignKey('PlayerModel',on_delete = models.CASCADE, blank=True, null=True)
    tour_playernumber = models.IntegerField(blank=True, null=True)
    tour_points = models.IntegerField(blank=True, null=True)
    tour_position = models.IntegerField(blank=True, null=True)
    tour_organizer = models.CharField(max_length=30, blank=True, null=True)

class PlayerStatsModel(models.Model):
    player_name = models.ForeignKey('PlayerModel',on_delete = models.CASCADE, blank=True, null=True) #models.CharField(max_length=30, blank=True, null=True) #

class TourCoursesModel(models.Model):
    tour_title = models.ForeignKey('TourModel',on_delete = models.CASCADE, blank=True, null=True)
    tour_course = models.CharField(max_length=50, blank=True, null=True)


class PlayerRegisterModel(models.Model):
    player_name = models.ForeignKey('PlayerModel', on_delete = models.CASCADE, blank=True, null=True)
    tour_status = models.CharField(choices=STATUS_OPTIONS, max_length=30, blank=True, null=True)
    comments = models.CharField(max_length=200, blank=True, null=True)

@receiver(post_save, sender=TourPlayerModel)
def player_status_udpate(sender, **kwargs):

    active_players = PlayerModel.objects.all()

    for player in active_players:
        tour_number = TourPlayerModel.objects.filter(tour_player__name=player.name).count()
        high_finish = list(TourPlayerModel.objects.filter(tour_player__name=player.name).aggregate(Min('tour_position')).values())[0]

        player, created = PlayerModel.objects.update_or_create(
            name=player.name, defaults = {
                'tour_number': tour_number,
                'high_finish': high_finish,
                })
