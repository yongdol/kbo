from django.db import models

from article.models import Team


class Teamrank(models.Model):
    team = models.ForeignKey(Team)
    rank = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    win_rate = models.FloatField(default=0.0)
    game_gap = models.FloatField(default=0.0)
    recent_10_game = models.CharField(max_length=10, blank=True)
    continuous = models.CharField(max_length=5, blank=True)
    home_score = models.CharField(max_length=10, blank=True)
    away_score = models.CharField(max_length=10, blank=True)
    standard_date = models.IntegerField(blank=True)

    def __str__(self):
        return self.team


class Hiterrank(models.Model):
    player = models.CharField(max_length=10)
    team = models.ForeignKey(Team)
    avg = models.FloatField(default=0.0)
    g = models.IntegerField(default=0)
    pa = models.IntegerField(default=0)
    ab = models.IntegerField(default=0)
    r = models.IntegerField(default=0)
    h = models.IntegerField(default=0)
    two_base = models.IntegerField(default=0)
    three_base = models.IntegerField(default=0)
    hr = models.IntegerField(default=0)
    total_base = models.IntegerField(default=0)
    rbi = models.IntegerField(default=0)
    sac = models.IntegerField(default=0)
    sf = models.IntegerField(default=0)
    bb = models.IntegerField(default=0)
    ibb = models.IntegerField(default=0)
    hbp = models.IntegerField(default=0)
    so = models.IntegerField(default=0)
    gdp = models.IntegerField(default=0)
    slg = models.FloatField(default=0.000)
    obp = models.FloatField(default=0.000)
    ops = models.FloatField(default=0.000)
    mh = models.IntegerField(default=0)
    risp = models.FloatField(default=0.000)
    ph_ba = models.FloatField(default=0.000)
    standard_date = models.IntegerField(blank=True)

    def __str__(self):
        return self.player































