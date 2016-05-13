#!/usr/bin/env python

from colors import *

class Player(object):
	def __init__(self, name='', tag='', color=None, setup='NO_SETUP'):
		self.name = name
		self.tag = tag
		self.color = color
		self.wins = 0
		self.losses = 0
		self.draws = 0

	def getMove(self):
		return -1

	def stats(self):
		return 'W/L/D: ' + str(self.wins) + '/' + str(self.losses) + '/' + str(self.draws)

	def addWin(self):
		self.wins += 1

	def addLoss(self):
		self.losses += 1

	def addDraw(self):
		self.draws += 1

	def coloredTag(self):
		return self.color + self.tag + colors['WHITE']

	def __str__(self):
		sb = []
		sb.append(self.name)
		sb.append(self.color + self.tag + colors['WHITE'])
		sb.append(self.stats())
		return ' - '.join(sb)
