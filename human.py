#!/usr/bin/env python

from player import Player
from colors import *

class HumanPlayer(Player):
		def __init__(self, name='', tag='', color=None, setup='NO_SETUP'):
			Player.__init__(self,name,tag,color,setup)

			if setup == 'MANUAL_SETUP':
				self.name = raw_input('Enter your name: ')

				self.tag = raw_input('Enter a tag (single character): ')

				while self.color == None:
					self.color = getColor(raw_input('Enter a color (type \'list\' to see a list of available colors): '))

		def getMove(self, board, opponent):
			return int(raw_input('enter a slot to drop a chip into (1-7): ')) - 1
