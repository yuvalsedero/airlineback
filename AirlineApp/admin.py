from django.contrib import admin
from .models import Airline_Companies, Countries, Users, Flights, Customers, Tickets, Administrators
# Register your models here.
admin.site.register(Airline_Companies)
admin.site.register(Countries)
admin.site.register(Users)
admin.site.register(Flights)
admin.site.register(Customers)
admin.site.register(Tickets)
admin.site.register(Administrators)
