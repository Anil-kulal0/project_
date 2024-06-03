# rates/admin.py
from django.contrib import admin
from .models import City, Rate

admin.site.register(City)
admin.site.register(Rate)


