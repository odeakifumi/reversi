#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import sys
import time

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


def init_board(need_handicap):
	board = [[0 for i in xrange(N)] for j in xrange(N)]
	board[3][3], board[4][4] = 2, 2
	board[4][3], board[3][4] = 1, 1
	if need_handicap:
		board[0][0], board[7][7] = 2, 2
		board[0][7], board[7][0] = 2, 2
	return board


def play_reversi():
	player1, player2 = 1, 2
	print '先手か後手かを決めてください'
	print '先手ならば 1 と、後手ならば 2 と、観戦をするならば 3 と、ハンデがいるなら4と、入力をしてください。'
	#入力されたモードが正しいかチェックする
	while True:
		input_mode = int(sys.stdin.readline().split()[0]) 
		if input_mode in [1, 2, 3, 4]:
			break
		else:
			print 'retry'

	if input_mode == 4:
		need_handicap = True
		input_mode = 2
	else:
		need_handicap = False
	board = init_board(need_handicap)
	display_board(board)
	r = True
	while True:
		if input_mode == player1:
			# ユーザーが打てるかどうか調べる
			if move.cpu_random_choice(board, me=player1, opp=player2) == (None, []):	
				choice, result = None, []
			else:
				choice, result = move.user_choice(board, me=player1, opp=player2)
		else:
			time.sleep(T)
			choice, result = move.cpu_random_choice(board, me=player1, opp=player2)#CPU同士で戦わせる
		if result:      
			board[choice[0]][choice[1]] = player1
			for pos in result:
				board[pos[0]][pos[1]] = player1
		else:
			print 'pass'
		if not (r or result):
			break
		#ここで指せるplayerを入れ替える
		player1, player2 = player2, player1 #player1は今指すことができる、pleyer2は今は指すことができない
		print "%s %s" % ("O" * board.count(1), "X" * board.count(2))


def simulation():
	ai_1_win = 0
	ai_2_win = 0
	for i in range(N_SIM):
		player1, player2 = 1, 2
		r = True
		ai_turn = i % 2 + 1
		board = init_board(need_handicap=False)
		while True:
			if ai_turn == player1:
				choice, result = move.cpu_ai_choice(board, me=player1, opp=player2)#CPU同士で戦わせる
			else:
				choice, result = move.cpu_random_choice(board, me=player1, opp=player2)#CPU同士で戦わせる
			if result:      
				board[choice[0]][choice[1]] = player1
				for pos in result:
					board[pos[0]][pos[1]] = player1
			if not (r or result):
				break
			r = result
			#ここで指せるplayerを入れ替える
			player1, player2 = player2, player1 #player1は今指すことができる、pleyer2は今は指すことができない
			ai_1_piece = (sum([y.count(1) for y in board]))
			ai_2_piece = (sum([y.count(2) for y in board]))
		if ai_1_piece > ai_2_piece:
			ai_1_win += 1
		elif ai_2_piece > ai_1_piece:
			ai_2_win += 1
	print ai_1_win / N_SIM
	print ai_2_win / N_SIM


def main():
	param = sys.argv
	if 2 <= len(param):
		if param[1] == 'play':
			play_reversi()
		elif param[1] == 'sim':
			simulation()
	else:
		print 'retry'
		print '[python reversi.py play]'
		print '[python reversi.py sim]'
		sys.exit()

if __name__ == '__main__':
	main()