#!/usr/bin/env python

import random
import copy

from ai import AIPlayer
from board import Board
import colors

class SimpleAIPlayer(AIPlayer):
	def __init__(self, name='Simple AI', tag='*', color=colors.colors['MAGENTA'], setup='NO_SETUP'):
		AIPlayer.__init__(self, name, tag, color, setup)
		random.seed()

	def will_win(self, board, col):
		will_win = False
		board.drop(self, col)
		if board.consecutive(self.target_length, self.tag()):
			will_win = True
		board.undo()
		return will_win

	def will_win_next(self, board, col):
		will_win_next = False
		board.drop(self, col)
		if board.legal(col):
			board.drop(self, col)
			if board.consecutive(self.target_length, self.tag()):
				will_win_next = True
			board.undo()
		board.undo()
		return will_win_next

	def will_lose(self, board, col, opponent):
		will_lose = False
		board.drop(opponent, col)
		if board.consecutive(self.target_length, opponent.tag()):
			will_lose = True
		board.undo()
		return will_lose

	def will_lose_next(self, board, col, opponent):
		will_lose_next = False
		board.drop(self, col)
		if board.legal(col):
			board.drop(opponent, col)
			if board.consecutive(self.target_length, opponent.tag()):
				will_lose_next = True
			board.undo()
		board.undo()
		return will_lose_next

	def move(self, board, opponent):
		move = random.randint(0, len(board.grid[0]))
		cols = list(range(0, len(board.grid[0])))
		random.shuffle(cols)
		for col in cols:
			if board.legal(col) and self.will_win(board, col):
				move = col
				break

		return move
