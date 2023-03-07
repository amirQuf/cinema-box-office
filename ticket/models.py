from django.db import models
from cinema.models import Showtime
from account.models import User

class Ticket(models.Model):
    showtime = models.ForeignKey(Showtime , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)