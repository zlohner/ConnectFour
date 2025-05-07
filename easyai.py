#!/usr/bin/env python

import random

from ai import AIPlayer
from board import Board
import colors

class EasyAIPlayer(AIPlayer):
	def __init__(self, name='Easy AI', tag='!', color=colors.colors['GREEN'], setup='NO_SETUP'):
		AIPlayer.__init__(self, name, tag, color, setup)
		random.seed()

	def move(self, board, opponent):
		return random.randint(0, len(board.grid[0]))
