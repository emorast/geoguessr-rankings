# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Games(models.Model):
    game_token = models.TextField(primary_key=True)
    map_name = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "games"


class Locations(models.Model):
    location = models.TextField(primary_key=True)
    map_name = models.TextField(blank=True, null=True)
    game_token = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    lng = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = "locations"


class Players(models.Model):
    user_id = models.TextField(primary_key=True)
    full_name = models.TextField(blank=True, null=True)
    played_games = models.IntegerField(blank=True, null=True)
    overall_elo = models.IntegerField(blank=True, null=True)
    seasonal_elo = models.IntegerField(blank=True, null=True)
    weekly_rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "players"


class Results(models.Model):
    user_id = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    game_token = models.TextField(blank=True, null=True)
    total_score = models.IntegerField(blank=True, null=True)
    score_1 = models.IntegerField(blank=True, null=True)
    score_2 = models.IntegerField(blank=True, null=True)
    score_3 = models.IntegerField(blank=True, null=True)
    score_4 = models.IntegerField(blank=True, null=True)
    score_5 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "results"
