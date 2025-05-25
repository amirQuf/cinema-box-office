from django.contrib import admin

from .models import Reservation,ReservedSeat


admin.site.register(Reservation)
admin.site.register(ReservedSeat)