from django.db import models

# Create your models here.

class Song(models.Model):
    songTitle = models.CharField(max_length=30)
    songDuration = models.TimeField()

class playlist(models.Model):
    playlistTitle = models.CharField(max_length=40)
    songid = models.ForeignKey('Song', on_delete=models.CASCADE)

class users(models.Model):
    username = models.CharField(max_length=40)
    # password = models
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)
    email = models.CharField()
    playlistid = models.ForeignKey('playlist', on_delete=models.CASCADE) # it should be many to many relationship

class artist(models.Model):
    # password = models
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)
    age = models.IntegerField()
    bio = models.CharField()
    songid = models.ForeignKey('Song', on_delete=models.CASCADE) #song has many artists chou mn3ml?
    album = models.ForeignKey('album', on_delete=models.CASCADE)

