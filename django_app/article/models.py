from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=10)
    nick_name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Article(models.Model):
    team = models.ForeignKey(Team)
    title = models.CharField(max_length=100)
    contents = models.CharField(max_length=500)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title