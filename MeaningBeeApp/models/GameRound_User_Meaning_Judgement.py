from django.db import models
from MeaningBeeApp.models import GameRound_User_Meaning_Mapping
from MeaningBeeApp.models import UserProfile
from MeaningBeeApp.models import WordMeaning

# Model to show the type of judgement given - Correct,Incorrect,Correct but not in dictionary and Unsure
class Judgement_Type(models.Model):

	CORRECT = "CORRECT"
	INCORRECT = "INCORRECT"
	CORRECT_NOT_IN_DICTIONARY = "CORRECT_NOT_IN_DICTIONARY"
	UNSURE = "UNSURE"
	TYPE_IN_CHOICES = (
		(CORRECT,"CORRECT"),
		(INCORRECT,"INCORRECT"),
		(CORRECT_NOT_IN_DICTIONARY,"CORRECT_NOT_IN_DICTIONARY"),
		(UNSURE,"UNSURE")
		)
	judgement_type = models.CharField(max_length=100,choices=TYPE_IN_CHOICES,default="UNSURE")

	def __unicode__(self):
		return self.judgement_type

# Model that shows the judgement given for specific meanings 
# given by users in specific rounds
class GameRound_User_Meaning_Judgement_Mapping(models.Model):
	# Indicates the specific meaning given by the user in a specific round
	gameround_user_meaning = models.ForeignKey(GameRound_User_Meaning_Mapping)
	# Indicates the user who has given the judgement for this meaning
	judge = models.ForeignKey(UserProfile)
	# Indicates the judgement - Correct/Incorrect/Not in dictionary,etc.
	judgement_type = models.ForeignKey(Judgement_Type)
	# Provides the system meaning for this particular word
	system_meaning = models.ForeignKey(WordMeaning)