from django.db import models
from django.utils import timezone

class Film(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    release_date = models.DateField(default = timezone.now )
    image =  models.ImageField(upload_to='Film')
    def __str__(self):
        return self.name


class  Theater(models.Model):
    name = models.CharField(max_length=70)
    capcity = models.PositiveIntegerField(default=0)
    number = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name

class Showtime(models.Model):
    film = models.ForeignKey(Film , on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    start_time = models.DateField(default = timezone.now )
    price = models.PositiveIntegerField(default=0)