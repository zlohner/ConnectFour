#!/usr/bin/env python

from game import Game
from board import Board
from player import Player
from human import HumanPlayer
from easyai import EasyAIPlayer
from simpleai import SimpleAIPlayer
from surviveai import SurviveAIPlayer
from aggressiveai import AggressiveAIPlayer
from minmaxai import MinMaxAIPlayer
from colors import *

NONE = '0'
ADD_PLAYER = '1'
SHOW_PLAYERS = '2'
START_GAME = '3'
RUN_SIMULATION = '4'
EXIT = '5'

class GameManager(object):

	def __init__(self):
		self.players = []
		self.players.append(EasyAIPlayer())
		self.players.append(SimpleAIPlayer())
		self.players.append(SurviveAIPlayer())
		self.players.append(AggressiveAIPlayer())
		self.players.append(MinMaxAIPlayer())
		self.players.append(MinMaxAIPlayer(name='MinMax AI (depth 5)', tag='$', color=colors['GREY'], maxDepth=5))
		self.game = None

	def menu(self):
		running = True
		while running:
			print ''
			print 'Welcome to Connect Four!'
			print ''
			print '(1) add a player'
			print '(2) show players'
			print '(3) play a game'
			print '(4) run simulation'
			print '(5) quit'
			print ''
			input = raw_input('What do you want to do? ')

			if input == ADD_PLAYER:
				self.players.append(HumanPlayer(setup='MANUAL_SETUP'))

			elif input == SHOW_PLAYERS:
				print '\n',self.playersStr()

			elif input == START_GAME:
				self.setupGame()
				self.playGame(True)

			elif input == RUN_SIMULATION:
				self.runSim()

			elif input == EXIT:
				running = False

			else:
				print 'Please enter a valid option (1-3)'

	def playersStr(self):
		sb = []
		for i in range(0,len(self.players)):
			sb.append('(' + str(i + 1) + ') ' + str(self.players[i]) + '\n')
		return ''.join(sb)

	def choosePlayer(self, num):
		player = -1
		while player > len(self.players) or player < 0:
			player = int(raw_input('Choose player ' + str(num) + '(1-' + str(len(self.players)) + '): ')) - 1
		return self.players[player]

	def setupGame(self):
		print '\n',self.playersStr()

		p1 = self.choosePlayer(1)
		p2 = self.choosePlayer(2)

		self.game = Game(board=Board(), player1=p1, player2=p2)

	def playGame(self, show):
		if self.game != None:
			self.game.playGame(show)

			if show:
				print '\n',self.game.board

			if self.game.winner != None:
				if show:
					print self.game.winner.coloredTag(),'wins!  '
				self.game.winner.addWin()
				self.game.loser.addLoss()
			else:
				if show:
					print 'it\'s a draw'
				self.game.currentPlayer.addDraw()
				self.game.nextPlayer.addDraw()

			self.game = None

	def runSim(self):
		print self.playersStr()

		p1 = self.choosePlayer(1)
		p2 = self.choosePlayer(2)

		numGames = int(raw_input('How many games should be played? '))

		for i in range(0, numGames):
			self.game = Game(board=Board(), player1=p1, player2=p2)
			self.playGame(True)


if __name__ == '__main__':
	manager = GameManager()
	manager.menu()
