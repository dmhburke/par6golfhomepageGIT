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
        USFlag = "https://cdn.webshopapp.com/shops/94414/files/54958226/the-united-states-flag-vector-free-download.jpg"
        AusFlag = "https://db-par6golfgeneral.s3.us-east-2.amazonaws.com/FlagImages/AusFlag.png"
        CanFlag = "https://db-par6golfgeneral.s3.us-east-2.amazonaws.com/FlagImages/CanFlag.png"
        EngFlag = "https://db-par6golfgeneral.s3.us-east-2.amazonaws.com/FlagImages/EngFlag.png"
        NZFlag = "https://db-par6golfgeneral.s3.us-east-2.amazonaws.com/FlagImages/NZFlag.jpg"
        SveFlag = "https://db-par6golfgeneral.s3.us-east-2.amazonaws.com/FlagImages/SveFlag.png"
        WalFlag = "https://db-par6golfgeneral.s3.us-east-2.amazonaws.com/FlagImages/WalesFlag.jpg"

        def get_flag(flag):
            switch_options = {
            "Australian": AusFlag,
            "American": USFlag,
            "English": EngFlag,
            "Canadian": CanFlag,
            "New Zealand": NZFlag,
            "Swedish": SveFlag,
            "Welsh": WalFlag
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
