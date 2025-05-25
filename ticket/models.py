from django.db import models
from cinema.models import Showtime ,Seat
from account.models import User

class Reservation(models.Model):
    class ReservationStatus(models.TextChoices):
        RESERVED = 'RESERVED', 'Reserved'
        CANCELLED = 'CANCELLED', 'Cancelled'
        COMPLETED = 'COMPLETED', 'Completed'
        EXPIRED = 'EXPIRED', 'Expired'
    show_time= models.ForeignKey(Showtime , on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE )
    reservation_time = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=ReservationStatus.choices,
        default=ReservationStatus.RESERVED
    )

class ReservedSeat(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    eat =   models.ForeignKey(Seat, on_delete=models.CASCADE)


