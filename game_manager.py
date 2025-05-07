#!/usr/bin/env python3

from game import Game
from board import Board
from player import Player
from human import HumanPlayer
from easyai import EasyAIPlayer
from simpleai import SimpleAIPlayer
from surviveai import SurviveAIPlayer
from aggressiveai import AggressiveAIPlayer
from minimaxai import MinimaxAIPlayer
import colors

NONE = '0'
ADD_PLAYER = '1'
SHOW_PLAYERS = '2'
START_GAME = '3'
RUN_SIMULATION = '4'
EXIT = '5'

class GameManager(object):

	def __init__(self):
		self.players = []
		self.players.append(HumanPlayer(name='Guest', tag='O', color=colors.color('WHITE')))
		self.players.append(EasyAIPlayer())
		self.players.append(SimpleAIPlayer())
		self.players.append(SurviveAIPlayer())
		self.players.append(AggressiveAIPlayer())
		self.players.append(MinimaxAIPlayer(name='Weak MinimaxAI'))
		self.players.append(MinimaxAIPlayer(name='Strong MinimaxAI', tag='@', color=colors.colors['GREY'], setup='NO_SETUP', maxTime=20))
		self.game = None

	def menu(self):
		running = True
		while running:
			print('')
			print('Welcome to Connect Four!')
			print('')
			print('(1) add a player')
			print('(2) show players')
			print('(3) play a game')
			print('(4) run simulation')
			print('(5) quit')
			print('')
			option = input('What do you want to do? ')

			if option == ADD_PLAYER:
				self.players.append(HumanPlayer(setup='MANUAL_SETUP'))

			elif option == SHOW_PLAYERS:
				print(f'\n{self.players_string()}')

			elif option == START_GAME:
				self.setup_game()
				self.play(True)

			elif option == RUN_SIMULATION:
				self.simulate()

			elif option == EXIT:
				running = False

			else:
				print('Please enter a valid option (1-5)')

	def players_string(self):
		sb = []
		for i in range(0,len(self.players)):
			sb.append('(' + str(i + 1) + ') ' + str(self.players[i]) + '\n')
		return ''.join(sb)

	def choose_player(self, num):
		player = -1
		while player >= len(self.players) or player < 0:
			player = int(input('Choose player ' + str(num) + '(1-' + str(len(self.players)) + '): ')) - 1
		return self.players[player]

	def setup_game(self):
		print(f'\n{self.players_string()}')

		p1 = self.choose_player(1)
		p2 = self.choose_player(2)

		self.game = Game(board=Board(), player1=p1, player2=p2)

	def play(self, show):
		if self.game != None:
			self.game.play(show)

			if show:
				print(f'\n{self.game.board}')

			if self.game.winner != None:
				if show:
					print(f'{self.game.winner.tag()} wins!  ')
				self.game.winner.add('W')
				self.game.loser.add('L')
			else:
				if show:
					print('it\'s a draw')
				self.game.current_player.add('D')
				self.game.next_player.add('D')

			self.game = None

	def simulate(self):
		print(self.players_string())

		p1 = self.choose_player(1)
		p2 = self.choose_player(2)

		numGames = int(input('How many games should be played? '))

		for i in range(0, numGames):
			self.game = Game(board=Board(), player1=p1, player2=p2)
			self.play(numGames == 1)


if __name__ == '__main__':
	manager = GameManager()
	manager.menu()
