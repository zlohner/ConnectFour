#!/usr/bin/env python

import random
import copy

from ai import AIPlayer
from board import Board
from colors import *

class SimpleAIPlayer(AIPlayer):
	def __init__(self, name='Simple AI', tag='*', color=colors['MAGENTA'], setup='NO_SETUP'):
		AIPlayer.__init__(self, name, tag, color, setup)
		random.seed()

	def willWin(self, board, col):
		willWin = False
		board.drop(self, col)
		if board.consecutive(self.winLength, self.coloredTag()):
			willWin = True
		board.undo()
		return willWin

	def willWinNext(self, board, col):
		willWinNext = False
		board.drop(self, col)
		if board.legalMove(col):
			board.drop(self, col)
			if board.consecutive(self.winLength, self.coloredTag()):
				willWinNext = True
			board.undo()
		board.undo()
		return willWinNext

	def willLose(self, board, col, opponent):
		willLose = False
		board.drop(opponent, col)
		if board.consecutive(self.winLength, opponent.coloredTag()):
			willLose = True
		board.undo()
		return willLose

	def willLoseNext(self, board, col, opponent):
		willLoseNext = False
		board.drop(self, col)
		if board.legalMove(col):
			board.drop(opponent, col)
			if board.consecutive(self.winLength, opponent.coloredTag()):
				willLoseNext = True
			board.undo()
		board.undo()
		return willLoseNext

	def getMove(self, board, opponent):
		move = random.randint(0, len(board.grid[0]))
		cols = range(0, len(board.grid[0]))
		random.shuffle(cols)
		for col in cols:
			if board.legalMove(col):
				if self.willWin(board, col):
					move = col
					break

		return move
