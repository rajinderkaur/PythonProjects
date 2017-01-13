from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)



    def __str__(self):
            return self.album_title + ' - ' + self.artist

#album is a foriegn key in song

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
# after you create the classes , go to the terminal inside website and run - python manage.py makemigrations music
# then run - python manage.py migrate : this will run the migrations and will create tables in the database
