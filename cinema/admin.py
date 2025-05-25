from django.contrib import admin

from .models import Paradise ,Film ,Showtime,Seat ,Salon


admin.site.register(Film)
admin.site.register(Paradise)
admin.site.register(Salon)
admin.site.register(Showtime)
admin.site.register(Seat)