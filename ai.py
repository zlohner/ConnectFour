#!/usr/bin/env python

import random

from player import Player
from colors import *

class AIPlayer(Player):
	def __init__(self, name='AI', tag='$', color=colors['GREY'], setup='NO_SETUP', winLength=4):
		Player.__init__(self, name, tag, color, setup)
		self.winLength = winLength
		random.seed()

	def getMove(self, board, opponent):
		return random.randint(0, len(board.grid[0]))
