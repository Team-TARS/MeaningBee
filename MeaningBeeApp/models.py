from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Feedback(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    date = models.DateTimeField("comment_date")

    def __unicode__(self):
        return self.username

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User, related_name="user_details")

    # Other fields here
    date_of_birth = models.DateTimeField()
    


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

