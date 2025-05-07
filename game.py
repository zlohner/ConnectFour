#!/usr/bin/env python

from board import Board
from player import Player
from human import HumanPlayer
import colors

class Game(object):
	def __init__(self, board, player1=None, player2=None, target_length=4):
		self.current_player = player1
		self.next_player = player2
		self.board = board
		self.target_length = target_length
		self.winner = None
		self.loser = None
		self.playing = True

	def play(self, show):
		while self.playing:
			if show:
				print(f'\n{self.board}')
			self.turn()

	def turn(self):
		slot = -1
		while not self.board.legal(slot):
			slot = self.current_player.move(self.board, self.next_player)

		self.board.drop(self.current_player, slot)
		if self.board.consecutive(self.target_length, self.current_player.tag()):
			self.playing = False
			self.winner = self.current_player
			self.loser = self.next_player
		elif self.board.draw():
			self.playing = False
		else:
			self.switch()

	def switch(self):
		swap = self.current_player
		self.current_player = self.next_player
		self.next_player = swap
