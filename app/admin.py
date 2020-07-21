from django.contrib import admin
from .models import Player, Course, Birdie

# Register your models here.
admin.site.register(Player)
admin.site.register(Course)
admin.site.register(Birdie)