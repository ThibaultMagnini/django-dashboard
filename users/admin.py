from django.contrib import admin
from .models import Profile, Team
# Register your models here.

admin.site.register(Profile)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']
