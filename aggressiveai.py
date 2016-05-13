#!/usr/bin/env python

import random
import copy

from simpleai import SimpleAIPlayer
from board import Board
from colors import *

class AggressiveAIPlayer(SimpleAIPlayer):
	def __init__(self, name='Aggressive AI', tag='#', color=colors['RED'], setup='NO_SETUP'):
		SimpleAIPlayer.__init__(self, name, tag, color, setup)
		random.seed()

	def getMove(self, board, opponent):
		move = random.randint(0, len(board.grid[0]))

		cols = range(0, len(board.grid[0]))
		random.shuffle(cols)

		for col in cols:
			if board.legalMove(col):
				if self.willWin(board, col):
					return col

		for col in cols:
			if board.legalMove(col):
				if self.willLose(board, col, opponent):
					return col

		for col in cols:
			if board.legalMove(col):
				if self.willWinNext(board, col):
					return col

		return move
