from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Feedback(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=1000)
#     date = models.DateTimeField("comment_date")

#     def __unicode__(self):
#         return self.username

# Model to identify the type of user - He could be admin/player 
class UserType(models.Model):
	ADMIN = 'ADMIN'
	PLAYER = 'PLAYER'

	TYPE_IN_CHOICES = (
		(ADMIN,'ADMIN'),
		(PLAYER,'PLAYER')
	)
	usertype_name = models.CharField(max_length=10,choices=TYPE_IN_CHOICES,default=PLAYER)


# Model that includes details of the user (firstname,lastname,email,etc.), DOB and user type
class UserProfile(models.Model):
    # This field is required. - One to one mapping with auth.user
    user = models.OneToOneField(User, related_name="user_details")
 #    ADMIN = 'AD'
 #    PLAYER = 'PL'
 #    TYPE_IN_CHOICES = (
	# 	(ADMIN,'ADMIN'),
	# 	(PLAYER,'PLAYER')
	# )

    # Other fields here
    # Date of birth of the user
    date_of_birth = models.DateTimeField()
    # Type (Admin/Player)
    usertype = models.ForeignKey(UserType)
