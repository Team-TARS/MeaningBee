from django.db import models

class Word(models.Model):
	word = models.CharField(max_length=200)

class WordMeaning(models.Model):
	word = models.ForeignKey(Word)
	part_of_speech = models.CharField(max_length=30)
	meaning = models.CharField(max_length=2000)
	isPlayerSuggested = models.BooleanField(default=False)
