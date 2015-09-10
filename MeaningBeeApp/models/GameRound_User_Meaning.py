from django.db import models
from MeaningBeeApp.models import GameRound_User_Mapping

# Model to map from every round to every single meaning 
# given by the users in that specific round
class GameRound_User_Meaning_Mapping(models.Model):
	# Indicates the specific user in the round
	game_round_user = models.ForeignKey(GameRound_User_Mapping)
	# Indicates the meaning given by the user in that round
	player_meaning = models.CharField(max_length=2000)
