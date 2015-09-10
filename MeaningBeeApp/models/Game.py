from django.db import models
from MeaningBeeApp.models import Word

# Model that indicates a specific game (that contains several rounds) 
class Game(models.Model):
	# Indicates game starting time 
	game_start = models.DateTimeField()
	# Indicates game ending time
	game_end = models.DateTimeField()

# Model that indicates specific rounds in a game
class GameRound(models.Model):
	game = models.ForeignKey(Game)
	# Indicates round starting time
	game_round_start = models.DateTimeField()
	# Indicates round ending time
	game_round_end = models.DateTimeField()
	# Indicates the word shown in that round
	word = models.ForeignKey(Word)



