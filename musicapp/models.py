from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField(default=1)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Song(models.Model):
    artiste = models.ForeignKey('Artiste', on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    date = models.DateTimeField('Date released') 
    likes = models.IntegerField(default=0)
    artist_id = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.CharField(max_length=1000)
  #  song_id = models.IntegerField()
    song_id= models.OneToOneField('Song', on_delete=models.CASCADE)
