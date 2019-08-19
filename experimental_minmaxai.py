#!/usr/bin/env python

import sys

from square import Square
from minmaxai import MinMaxAIPlayer
from colors import *

class ExperimentalMinMaxAIPlayer(MinMaxAIPlayer):
	def __init__(self, name='Experimental MinMax AI', tag='@', color=colors['GREY'], setup='NO_SETUP', maxTime=20):
		MinMaxAIPlayer.__init__(self, name, tag, color, setup)

	def evaluate(self, board, opponent, depth):
		evaluation = 0
		for x in range(len(board.grid)):
			for y in range(len(board.grid[0])):
				if board.consecutive((self.winLength - 1), self.coloredTag(), position=(x,y), gaps=1):
					evaluation += 3
				if board.consecutive((self.winLength - 1), opponent.coloredTag(), position=(x,y), gaps=1):
					evaluation -= 3
				if board.consecutive((self.winLength - 1), self.coloredTag(), position=(x,y), gaps=2):
					evaluation += 1
				if board.consecutive((self.winLength - 1), opponent.coloredTag(), position=(x,y), gaps=2):
					evaluation -= 1

		return evaluation
