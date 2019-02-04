#!/usr/bin/env python

from square import Square

class Board(object):
	def __init__(self, col=7, row=6):
		self.grid = []
		for r in range(row):
			nextRow = []
			for c in range(col):
				nextRow.append(Square())
			self.grid.append(nextRow)
		self.playedLocations = []

	def findOpen(self, col):
		for r in range(-1, -(len(self.grid) + 1), -1):
			if self.grid[r][col].tag == ' ':
				return r % len(self.grid)
		return -1

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

	def consecutiveCol(self, n, position):
		(x, y) = position
		count = 0
		while len(self.grid) > (x + count) and self.grid[x + count][y] == self.grid[x][y]:
			count += 1

		return count >= n

	def consecutiveRow(self, n, position):
		(x, y) = position
		start = y
		while start >= 0 and self.grid[x][start] == self.grid[x][y]:
			start -= 1
		start += 1

		count = 0
		while len(self.grid[x]) > (start + count) and self.grid[x][start + count] == self.grid[x][y]:
			count += 1

		return count >= n

	def consecutiveDownDiagonal(self, n, position):
		(x, y) = position
		startRow = x
		startCol = y
		while startRow >= 0 and startCol >= 0 and self.grid[startRow][startCol] == self.grid[x][y]:
			startRow -= 1
			startCol -= 1
		startRow += 1
		startCol += 1

		count = 0
		while len(self.grid) > (startRow + count) and len(self.grid[x]) > (startCol + count) and self.grid[startRow + count][startCol + count] == self.grid[x][y]:
			count += 1

		return count >= n

	def consecutiveUpDiagonal(self, n, position):
		(x, y) = position
		startRow = x
		startCol = y
		while len(self.grid) > startRow and startCol >= 0 and self.grid[startRow][startCol] == self.grid[x][y]:
			startRow += 1
			startCol -= 1
		startRow -= 1
		startCol += 1

		count = 0
		while (startRow - count) >= 0 and len(self.grid[x]) > (startCol + count) and self.grid[startRow - count][startCol + count] == self.grid[x][y]:
			count += 1

		return count >= n

	def consecutive(self, n, position=None):
		if position == None:
			if len(self.playedLocations) == 0:
				return False
			position = self.playedLocations[-1]
		return self.consecutiveCol(n, position) or self.consecutiveRow(n, position) or self.consecutiveDownDiagonal(n, position) or self.consecutiveUpDiagonal(n, position)

	def draw(self):
		draw = True
		for i in range(0, len(self.grid[0])):
			draw = draw and not self.legalMove(i)
		return draw

	def __str__(self):
		s = []
		for row in self.grid:
			s.append('|')
			for col in row:
				s.append(str(col))
				s.append('|')
			s.append('\n')
		return ''.join(s)
