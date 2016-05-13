#!/usr/bin/env python

import random
import copy

from simpleai import SimpleAIPlayer
from board import Board
from colors import *

class SurviveAIPlayer(SimpleAIPlayer):
	def __init__(self, name='Survive AI', tag='%', color=colors['YELLOW'], setup='NO_SETUP'):
		SimpleAIPlayer.__init__(self, name, tag, color, setup)
		random.seed()

	def getMove(self, board, opponent):
		move = -1

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
				if move == -1 and not self.willLoseNext(board, move, opponent):
					return col

		return move
