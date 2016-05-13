#!/usr/bin/env python

import sys
import random

from square import Square
from ai import AIPlayer
from colors import *

class MinMaxAIPlayer(AIPlayer):
	def __init__(self, name='MinMax AI (depth 4)', tag='&', color=colors['BLUE'], setup='NO_SETUP', maxDepth=4):
		AIPlayer.__init__(self, name, tag, color, setup)
		self.maxDepth = maxDepth
		random.seed()

	def value(self, board, opponent):
		if board.consecutive(n=self.winLength):
			(x,y) = board.playedLocations[-1]
			if board.grid[x][y].tag == self.coloredTag():
				return sys.maxsize
			else:
				return -sys.maxsize
		else:
			value = 0
			for j in range(0, len(board.grid[0])):
				for i in range(len(board.grid) - 1, -1, -1):
					if board.grid[i][j].tag == ' ':

						endSquare = False
						board.grid[i][j] = Square(self.coloredTag())
						if board.consecutive(n=self.winLength, position=(i,j)):
							endSquare = True
							value += 1
						if board.consecutive(n=self.winLength - 1, position=(i,j)):
							value += 1

						dualEndSquare = False
						board.grid[i][j] = Square(opponent.coloredTag())
						if board.consecutive(n=self.winLength - 1, position=(i,j)):
							if endSquare:
								dualEndSquare = True
							value -= 1
						if board.consecutive(n=self.winLength, position=(i,j)):
							value -= 1

						board.grid[i][j] = Square()
						if dualEndSquare:
							break
			return value


	def minimax(self, board, opponent, depth, max):
		if depth == 0 or board.consecutive(n=self.winLength):
			return (self.value(board, opponent), -1)

		bestValue = 0
		bestMove = -1

		cols = range(0, len(board.grid[0]))
		random.shuffle(cols)

		if max:
			bestValue = 2 * (-sys.maxsize)
			bestMove = -1
			for i in cols:
				if board.legalMove(i):
					board.drop(self, i)
					(v, move) = self.minimax(board, opponent, depth - 1, False)

					# prioritize winning faster
					if v > sys.maxsize - self.maxDepth:
						v -= 1

					# prolong if losing
					if v < -sys.maxsize + self.maxDepth:
						v += 1

					if v > bestValue:
						bestValue = v
						bestMove = i
					board.undo()

			return (bestValue, bestMove)
		else:
			bestValue = 2 * sys.maxsize
			for i in cols:
				if board.legalMove(i):
					board.drop(opponent, i)
					(v, move) = self.minimax(board, opponent, depth - 1, True)

					# prioritize winning faster
					if v < -sys.maxsize - self.maxDepth:
						v -= 1

					# prolong if losing
					if v > sys.maxsize + depth:
						v += 1

					if v < bestValue:
						bestValue = v
						bestMove = i
					board.undo()

			return (bestValue, bestMove)



	def getMove(self, board, opponent):
		(bestValue, bestMove) = self.minimax(board, opponent, self.maxDepth, True)

		if bestValue < 0:
			print 'I\'m losing :('
		elif bestValue > 0:
			print 'I\'m winning :)'
		else:
			print 'This is a close one!'

		return bestMove
