#!/usr/bin/env python

import random

from ai import AIPlayer
from board import Board
from colors import *

class EasyAIPlayer(AIPlayer):
	def __init__(self, name='Easy AI', tag='!', color=colors['GREEN'], setup='NO_SETUP'):
		AIPlayer.__init__(self, name, tag, color, setup)
		random.seed()

	def getMove(self, board, opponent):
		return random.randint(0, len(board.grid[0]))
