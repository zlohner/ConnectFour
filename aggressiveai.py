#!/usr/bin/env python

import random
import copy

from simpleai import SimpleAIPlayer
from board import Board
import colors

class AggressiveAIPlayer(SimpleAIPlayer):
	def __init__(self, name='Aggressive AI', tag='#', color=colors.colors['RED'], setup='NO_SETUP'):
		SimpleAIPlayer.__init__(self, name, tag, color, setup)
		random.seed()

	def move(self, board, opponent):
		move = random.randint(0, len(board.grid[0]))

		cols = list(range(0, len(board.grid[0])))
		random.shuffle(cols)

		for col in cols:
			if board.legal(col):
				if self.will_win(board, col):
					return col

		for col in cols:
			if board.legal(col):
				if self.will_lose(board, col, opponent):
					return col

		for col in cols:
			if board.legal(col):
				if self.will_win_next(board, col):
					return col

		return move
