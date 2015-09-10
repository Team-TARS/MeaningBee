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
