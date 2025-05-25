from django.db import models
from django.utils import timezone
from account.models import User
class Film(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    release_date = models.DateField(default = timezone.now )
    image =  models.ImageField(upload_to='Film')
    time =  models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class  Paradise(models.Model):
    name = models.CharField(max_length=70)
    address  = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Salon(models.Model):
    paradise = models.ForeignKey(Paradise , on_delete=models.CASCADE)
    name = models.PositiveIntegerField(default=0)
    capacity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.paradise.name}|{self.name}" 
    
class Showtime(models.Model):
    film = models.ForeignKey(Film , on_delete=models.CASCADE)
    paradise = models.ForeignKey(Paradise, on_delete=models.CASCADE)
    Salon = models.ForeignKey(Salon , on_delete=models.CASCADE)
    start_time = models.DateField(default = timezone.now )
    end_time = models.DateField(default = timezone.now )
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.film.name} | {self.paradise.name}'
    

class Seat(models.Model):
    salon = models.ForeignKey(Salon , on_delete=models.CASCADE)
    paradise =models.ForeignKey(Paradise, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'{self.paradise.name} | {self.Salon.name}|{self.number}'
    

