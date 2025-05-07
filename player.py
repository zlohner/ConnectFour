#!/usr/bin/env python

import colors

class Player(object):
	def __init__(self, name='', tag='', color=None, setup='NO_SETUP'):
		self.name = name
		self._tag = tag
		self.color = color
		self.wins = 0
		self.losses = 0
		self.draws = 0

	def move(self):
		return -1

	def stats(self):
		return 'W/L/D: ' + str(self.wins) + '/' + str(self.losses) + '/' + str(self.draws)
	
	def add(self, stat):
		if stat == 'W':
			self.wins += 1
		if stat == 'L':
			self.losses += 1
		if stat == 'D':
			self.draws += 1

	def tag(self):
		return self.color + self._tag + colors.colors['WHITE']

	def __str__(self):
		sb = []
		sb.append(self.name)
		sb.append(self.tag())
		sb.append(self.stats())
		return ' - '.join(sb)
