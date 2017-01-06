from django.contrib import admin

# Register your models here.
from .models import Album

#make album table appear in admin
admin.site.register(Album)