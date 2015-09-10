from django.db import models
from MeaningBeeApp.models import UserProfile
from MeaningBeeApp.models import GameRound

# Model to map between the game round and the users playing that round
class GameRound_User_Mapping(models.Model):
	# The user in the game round
	user = models.ForeignKey(UserProfile)
	# The round to which he belongs to (Ex : 4 people (user 1,2,3 and 4) will have game_round ID 1)
	game_round = models.ForeignKey(GameRound)
	# Indicates whether the round has finished the meaning phase (ie all players have completed the meanig phase)
	is_meaning_completed = models.BooleanField(default=False)
	# Indicates whether the round has finished the judging phase (ie all players have completed the judging phase)
	is_judging_completed = models.BooleanField(default=False)
	# Overall judging score of the player in this round
	judging_score = models.IntegerField()
	# Overall meaning score of the player in this round
	meaning_score = models.IntegerField()
