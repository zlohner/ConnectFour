#!/usr/bin/env python

import sys
from time import time

from square import Square
from ai import AIPlayer
from colors import *

class MinMaxAIPlayer(AIPlayer):
	def __init__(self, name='MinMax AI', tag='&', color=colors['BLUE'], setup='NO_SETUP', maxTime=5):
		AIPlayer.__init__(self, name, tag, color, setup)
		self.mem = {}
		self.maxTime = maxTime

	def evaluate(self, board, opponent, depth):
		if board.consecutive(self.winLength, self.coloredTag()):
			return (sys.maxsize - depth)
		elif board.consecutive(self.winLength, opponent.coloredTag()):
			return (-sys.maxsize + depth)
		else:
			evaluation = 0
			for y in range(len(board.grid[0])):
				for x in range((len(board.grid) - 1), -1, -1):
					if (board.open((x, y))):
						myThreat = board.consecutiveThrough(self.winLength, self.coloredTag(), position=(x,y))
						oppThreat = board.consecutiveThrough(self.winLength, opponent.coloredTag(), position=(x,y))

						if myThreat and oppThreat:
							break
						elif myThreat:
							evaluation += 1
						elif oppThreat:
							evaluation -= 1

			return evaluation

	def minimax(self, board, opponent, maxDepth, depth=0, alpha=-sys.maxsize, beta=sys.maxsize, max=True):
		key = (board.key(), max, depth, maxDepth)
		if not key in self.mem:
			if board.consecutive(self.winLength, self.coloredTag()):
				self.mem[key] = ((sys.maxsize - depth), -1)
			elif board.consecutive(self.winLength, opponent.coloredTag()):
				self.mem[key] = ((-sys.maxsize + depth), -1)
			elif not any([board.legalMove(i) for i in range(0, len(board.grid[0]))]):
				self.mem[key] = (0, -1)
			elif depth == maxDepth:
				self.mem[key] = (self.evaluate(board, opponent, depth), -1)
			else:
				cols = [3, 2, 4, 1, 5, 0, 6]
				value = 0
				move = -1

				if max:
					value = -sys.maxsize
					for i in cols:
						if board.legalMove(i) and alpha < beta:
							board.drop(self, i)
							(v, m) = self.minimax(board, opponent, maxDepth, (depth + 1), alpha, beta, False)
							board.undo()

							if v > value:
								value = v
								move = i

							if value > alpha:
								alpha = value

				else:
					value = sys.maxsize
					for i in cols:
						if board.legalMove(i) and alpha < beta:
							board.drop(opponent, i)
							(v, m) = self.minimax(board, opponent, maxDepth, (depth + 1), alpha, beta, True)
							board.undo()

							if v < value:
								value = v
								move = i

							if value < beta:
								beta = value

				self.mem[key] = (value, move)

		return self.mem[key]

	def getMove(self, board, opponent):
		start = time()
		depth = 0

		while (time() - start) < self.maxTime:
			depth += 1
			(value, move) = self.minimax(board, opponent, depth)
			if \
				depth > board.remainingMoves() or \
				value >= sys.maxsize - board.remainingMoves() or \
				value <= -sys.maxsize + board.remainingMoves():
				break

		print 'evaluated to depth:', depth
		print 'move:', (move + 1)
		if value >= (sys.maxsize - board.remainingMoves()):
			evaluation = 'win in %d moves' % (depth - 1)
		elif value > 3:
			evaluation = 'advantaged'
		elif value > 0:
			evaluation = 'slightly advantaged'
		elif value <= (-sys.maxsize + board.remainingMoves()):
			evaluation = 'loss in %d moves' % (depth - 1)
		elif value < -3:
			evaluation = 'disadvantaged'
		elif value < 0:
			evaluation = 'slightly disadvantaged'
		else:
			evaluation = 'equal'
		print 'evaluation:', evaluation

		return move
