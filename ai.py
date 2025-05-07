#!/usr/bin/env python

import random

from player import Player
import colors

class AIPlayer(Player):
	def __init__(self, name='AI', tag='$', color=colors.colors['GREY'], setup='NO_SETUP', target_length=4):
		Player.__init__(self, name, tag, color, setup)
		self.target_length = target_length
		random.seed()

	def move(self, board, opponent):
		return random.randint(0, len(board.grid[0]))
