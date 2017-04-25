from django.db import models

from article.models import Team


class TeamRank(models.Model):
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
    standard_date = models.CharField(max_length=32)

    def __str__(self):
        return self.team
