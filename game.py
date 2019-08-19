#!/usr/bin/env python

from board import Board
from player import Player
from human import HumanPlayer
from colors import *

class Game(object):
	def __init__(self, board, player1=HumanPlayer('X', getColor('RED')), player2=HumanPlayer('O', getColor('BLUE')), winLength=4):
		self.currentPlayer = player1
		self.nextPlayer = player2
		self.board = board
		self.winLength = winLength
		self.winner = None
		self.loser = None
		self.playing = True

	def playGame(self, show):
		while self.playing:
			if show:
				print '\n',self.board
			self.doTurn()

	def doTurn(self):
		slot = -1
		while not self.board.legalMove(slot):
			slot = self.currentPlayer.getMove(self.board, self.nextPlayer)

		self.board.drop(self.currentPlayer, slot)
		if self.board.consecutive(self.winLength, self.currentPlayer.coloredTag()):
			self.playing = False
			self.winner = self.currentPlayer
			self.loser = self.nextPlayer
		elif self.board.draw():
			self.playing = False
		else:
			self.switchTurn()


	def switchTurn(self):
		swap = self.currentPlayer
		self.currentPlayer = self.nextPlayer
		self.nextPlayer = swap
