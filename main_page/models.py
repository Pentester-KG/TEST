from django.db import models


class Deviz(models.Model):
    title = models.CharField(max_length=100)


class Video(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(verbose_name='Ссылка для видео')


class TopTechnics(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(verbose_name='decription')
    price = models.PositiveIntegerField(default=1000)
    image = models.ImageField()


