#!/usr/bin/env python

import sys
from time import time

from ai import AIPlayer
import colors

class MinimaxAIPlayer(AIPlayer):
	def __init__(self, name='Minimax AI', tag='&', color=colors.colors['BLUE'], setup='NO_SETUP', maxTime=5):
		AIPlayer.__init__(self, name, tag, color, setup)
		self.mem = {}
		self.maxTime = maxTime

	def evaluate(self, board, opponent, depth):
		if board.consecutive(self.target_length, self.tag()):
			return (sys.maxsize - depth)
		elif board.consecutive(self.target_length, opponent.tag()):
			return (-sys.maxsize + depth)
		else:
			evaluation = 0
			for y in range(len(board.grid[0])):
				for x in range((len(board.grid) - 1), -1, -1):
					if (board.open((x, y))):
						my_threat = board.consecutive_through(self.target_length, self.tag(), position=(x,y))
						opp_threat = board.consecutive_through(self.target_length, opponent.tag(), position=(x,y))

						if my_threat and opp_threat:
							break
						elif my_threat:
							evaluation += 1
						elif opp_threat:
							evaluation -= 1

			return evaluation

	def minimax(self, board, opponent, max_depth, depth=0, alpha=-sys.maxsize, beta=sys.maxsize, max=True):
		key = (board.key(), max, depth, max_depth)
		if not key in self.mem:
			if board.consecutive(self.target_length, self.tag()):
				self.mem[key] = ((sys.maxsize - depth), -1)
			elif board.consecutive(self.target_length, opponent.tag()):
				self.mem[key] = ((-sys.maxsize + depth), -1)
			elif not any([board.legal(i) for i in range(0, len(board.grid[0]))]):
				self.mem[key] = (0, -1)
			elif depth == max_depth:
				self.mem[key] = (self.evaluate(board, opponent, depth), -1)
			else:
				cols = [3, 2, 4, 1, 5, 0, 6]
				value = 0
				move = -1

				if max:
					value = -sys.maxsize
					for i in cols:
						if board.legal(i) and alpha < beta:
							board.drop(self, i)
							(v, m) = self.minimax(board, opponent, max_depth, (depth + 1), alpha, beta, False)
							board.undo()

							if v > value:
								value = v
								move = i

							if value > alpha:
								alpha = value

				else:
					value = sys.maxsize
					for i in cols:
						if board.legal(i) and alpha < beta:
							board.drop(opponent, i)
							(v, m) = self.minimax(board, opponent, max_depth, (depth + 1), alpha, beta, True)
							board.undo()

							if v < value:
								value = v
								move = i

							if value < beta:
								beta = value

				self.mem[key] = (value, move)

		return self.mem[key]

	def move(self, board, opponent):
		start = time()
		depth = 0

		while (time() - start) < self.maxTime:
			depth += 1
			(value, move) = self.minimax(board, opponent, depth)
			if \
				depth > board.remaining_moves() or \
				value >= sys.maxsize - board.remaining_moves() or \
				value <= -sys.maxsize + board.remaining_moves():
				break

		print(f'evaluated to depth: {depth}')
		print(f'move: {move + 1}')
		if value >= (sys.maxsize - board.remaining_moves()):
			evaluation = 'win in %d moves' % (depth - 1)
		elif value > 3:
			evaluation = 'advantaged'
		elif value > 0:
			evaluation = 'slightly advantaged'
		elif value <= (-sys.maxsize + board.remaining_moves()):
			evaluation = 'loss in %d moves' % (depth - 1)
		elif value < -3:
			evaluation = 'disadvantaged'
		elif value < 0:
			evaluation = 'slightly disadvantaged'
		else:
			evaluation = 'equal'
		print(f'evaluation: {evaluation}')

		return move
