from django.contrib import admin

# Register your models here.
from .models import Album, Song

#make album table appear in admin
admin.site.register(Album)
admin.site.register(Song)