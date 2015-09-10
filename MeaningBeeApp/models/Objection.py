from django.db import models
from MeaningBeeApp.models import UserProfile
from MeaningBeeApp.models import GameRound_User_Meaning_Judgement_Mapping

# Model that shows any objections raised, if any
class Objection(models.Model):
	# Indicates the user who has raised the objection
	raised_by = models.ForeignKey(UserProfile,related_name='%(class)s_raised_by')
	# Indicates the user/admin who addressed the objection
	addressed_by = models.ForeignKey(UserProfile,related_name='%(class)s_addressed_by')
	# Indicates whether the score of the user changed because of this objection
	isScoreChanged = models.BooleanField(default=False)
	# Indicates the original judgement that was provided for the meaning the user had provided
	gameround_user_meaning_judgement = models.ForeignKey(GameRound_User_Meaning_Judgement_Mapping)
