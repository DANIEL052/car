from django.contrib import admin
from .models import Person, Car, Rent
from django.contrib.sessions.models import Session

admin.site.register(Session)
admin.site.register(Person)
admin.site.register(Car)
admin.site.register(Rent)
