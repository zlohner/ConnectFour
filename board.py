#!/usr/bin/env python

from square import Square

class Board(object):
	def __init__(self, col=7, row=6):
		self.grid = [[Square() for c in range(col)] for r in range(row)]
		self.playedLocations = []

	def open(self, position):
		(x, y) = position
		if x >= len(self.grid) or y >= len(self.grid[x]) or x < 0 or y < 0:
			return False
		return self.grid[x][y].tag == ' '

	def findOpen(self, col):
		for r in range(-1, -(len(self.grid) + 1), -1):
			if self.open(((r % len(self.grid)), col)):
				return r % len(self.grid)
		return -1

	def remainingMoves(self):
		count = 0
		for x in range(len(self.grid)):
			for y in range(len(self.grid[x])):
				if self.open((x, y)):
					count += 1
		return count

	def drop(self, player, col):
		row = self.findOpen(col)
		self.playedLocations.append((row, col))
		self.grid[row][col] = Square(player.coloredTag())

	def undo(self):
		(row, col) = self.playedLocations[-1]
		self.grid[row][col] = Square()
		self.playedLocations = self.playedLocations[:-1]

	def legalMove(self, col):
		if col >= 0 and col < len(self.grid[0]):
			row = self.findOpen(col)
			return row != -1
		else:
			return False

	def consecutive(self, n, tag, position=None, delta=None, gaps=0):
		if position == None:
			for x in range(len(self.grid)):
				for y in range(len(self.grid[x])):
					if self.consecutive(n, tag, (x, y)):
						return True
			return False

		if delta == None:
			return \
				self.consecutive(n, tag, position, (1, 0)) or \
				self.consecutive(n, tag, position, (0, 1)) or \
				self.consecutive(n, tag, position, (1, 1)) or \
				self.consecutive(n, tag, position, (-1, 1))
		else:
			(x, y) = position
			(dx, dy) = delta
			if x >= len(self.grid) or y >= len(self.grid[x]) or x < 0 or y < 0:
				return False
			if tag and self.grid[x][y].tag != tag:
				if self.open((x, y)):
					gaps -= 1
					if gaps < 0:
						return False
				else:
					return False
			if n == 1:
				return True
			return self.consecutive(n - 1, tag, ((x + dx), (y + dy)), delta, gaps)

	def consecutiveThrough(self, n, tag, position):
		(x, y) = position
		return \
			any([self.consecutive(n, tag, position=(x - k, y), delta=(1, 0), gaps=1) for k in range(n)]) or \
			any([self.consecutive(n, tag, position=(x, y - k), delta=(0, 1), gaps=1) for k in range(n)]) or \
			any([self.consecutive(n, tag, position=(x - k, y - k), delta=(1, 1), gaps=1) for k in range(n)]) or \
			any([self.consecutive(n, tag, position=(x + k, y - k), delta=(-1, 1), gaps=1) for k in range(n)])

	def draw(self):
		return not any([self.legalMove(i) for i in range(len(self.grid[0]))])

	def key(self):
		s = []
		for row in self.grid:
			for col in row:
				s.append(col.key())
		return ''.join(s)

	def __str__(self):
		s = []
		for row in self.grid:
			s.append('|')
			for col in row:
				s.append(str(col))
				s.append('|')
			s.append('\n')
		return ''.join(s)
