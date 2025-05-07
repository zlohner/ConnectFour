#!/usr/bin/env python

import colors
from player import Player

class HumanPlayer(Player):
		def __init__(self, name='', tag='', color=None, setup='NO_SETUP'):
			Player.__init__(self, name, tag, color, setup)

			if setup == 'MANUAL_SETUP':
				self.name = input('Enter your name: ')

				self._tag = input('Enter a tag (single character): ')

				while self.color == None:
					self.color = colors.color(input('Enter a color (type \'list\' to see a list of available colors): '))

		def move(self, board, opponent):
			return int(input('enter a slot to drop a chip into (1-7): ')) - 1
