from django.db import models

# Create your models here.


class Feedback(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    date = models.DateTimeField("comment_date")

    def __unicode__(self):
        return self.username


