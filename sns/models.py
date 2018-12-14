from django.db import models

# Create your models here.
class NewTweet(models.Model):
    tweet = models.CharField(max_length=240)