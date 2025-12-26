from django.contrib import admin
from .models import Film, Genre, Director, Review

admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Review)
