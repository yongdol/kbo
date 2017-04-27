from django.db import models


class Team(models.Model):
    full_name = models.CharField(max_length=10)
    short_name = models.CharField(max_length=3)
    nick_name = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    team = models.ForeignKey(Team)
    date = models.IntegerField(blank=True)
    title = models.CharField(max_length=100, blank=True)
    contents = models.CharField(max_length=500, blank=True)
    link = models.URLField(blank=True, unique=True)
    img = models.URLField(blank=True)

    def __str__(self):
        return self.title

