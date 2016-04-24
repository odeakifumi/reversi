#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from config import *
import move


def display_board(board):
	print '  a b c d e f g h'
	for i in xrange(N):
		print i,
		for j in xrange(N):
			print SQUARE_TYPE[board[i][j]],
		print
	print


def play_reversi():
	player1, player2 = 1, 2
	r = []
	print '先手か後手かを決めてください'
	print '先手ならば 1 と、後手ならば 2 と、観戦をするならば 3 と、入力をしてください。'
	while True:
		input_mode = sys.stdin.readline().split()[0]
		c = ['1','2','3']
		if input_mode in c:
			if input_mode == '1':
				break
			if input_mode == '2':
				break
			if input_mode == '3':
				break
		else:
			print 'retry'
	board = [[0 for i in xrange(N)] for j in xrange(N)]
	board[3][3], board[4][4] = 1, 1
	board[4][3], board[3][4] = 2, 2
	display_board(board)
	while True:
		if int(input_mode) == player1:
			choice, result = move.cpu_choice(board, me=player1, opp=player2)
			choice, result = move.user_choice(board, me=player1, opp=player2)
		else:
			choice, result = move.cpu_choice(board, me=player1, opp=player2)
		if result:
			board[choice[0]][choice[1]] = player1
			for pos in result:
				board[pos[0]][pos[1]] = player1
		if not (r or result):
			break
		r = result
		display_board(board)
		#ここで指せるplayerを入れ替える
		player1, player2 = player2, player1 #player1は今指すことができる、pleyer2は今は指すことができない
	print "%s %s" % ("O" * board.count(1), "X" * board.count(2))


def main():
	play_reversi()

if __name__ == '__main__':
	main()