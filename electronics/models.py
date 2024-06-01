from django.db import models
from django.views import generic


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Electronics(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/')
    feature = models.CharField(max_length=150, default='Данные отсутсвуют')
    tags = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



