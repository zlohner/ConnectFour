#!/usr/bin/env python

import random

from simpleai import SimpleAIPlayer
import colors

class SurviveAIPlayer(SimpleAIPlayer):
	def __init__(self, name='Survive AI', tag='%', color=colors.colors['YELLOW'], setup='NO_SETUP'):
		SimpleAIPlayer.__init__(self, name, tag, color, setup)
		random.seed()

	def move(self, board, opponent):
		move = -1

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
				if move == -1 and not self.will_lose_next(board, move, opponent):
					return col

		return move
