
import colors
from player import Player
from board import Board

def test_drop():
	b = Board()
	p1 = Player('test', 'X', colors.color('RED'))
	p2 = Player('test', 'O', colors.color('BLUE'))
	players = [p1, p2]
	expected_remaining_moves = 42
	for i in range(7):
		for j in range(6):
			assert b.remaining_moves() == expected_remaining_moves
			assert b.find_open(i) != -1
			b.drop(players[j % 2], i)
			expected_remaining_moves -= 1

	for i in range(7):
		assert b.find_open(i) == -1
