#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from random import randint

N = 8
SQUARE_TYPE=('.', 'O', 'X') #変更できないリスト
kihu_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}

# コメントを残そう


def display_board(board):
	print '  a b c d e f g h'
	for i in xrange(N):
		print i,
		for j in xrange(N):
			print SQUARE_TYPE[board[i][j]],
		print
	print


def think_choice(board, me, opp):
	choice, result = None, []
	# for pos in xrange(64):
	for x in xrange(N):
		for y in xrange(N):
			if board[x][y] != 0:  # 既に駒が存在
				continue
			cand = []
			# scan all directions
			for xx, yy in ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)):
				cand_tmp = []
				distance = 1
				while True:
					xt = x + xx * distance
					yt = y + yy * distance
					if xt >= N or xt < 0 or yt >= N or yt < 0:
						break
					if board[xt][yt] == opp:
						cand_tmp.append((xt, yt))
						distance += 1
						continue
					if board[xt][yt] == me and cand_tmp:
						cand.extend(cand_tmp)
						break
					break
				if not cand:
					continue
				# nearly random strategy :)
				if (x, y) in ((0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1)):
					return (x, y), cand  # sumikko!
				if len(cand) + randint(0, 1) > len(result):
					choice, result = (x, y), cand
	return choice, result


def play_othello():
	board = [[0 for i in xrange(N)] for j in xrange(N)]
	board[3][3], board[4][4] = 1, 1
	board[4][3], board[3][4] = 2, 2
	display_board(board)
	player1, player2 = 1, 2
	r = []
	while 1:
		choice, result = think_choice(board, me=player1, opp=player2)
		if result:
			board[choice[0]][choice[1]] = player1
			for pos in result:
				board[pos[0]][pos[1]] = player1
		if not (r or result):
			break
		r = result
		display_board(board)
		player1, player2 = player2, player1
		while True:
			input_lines = sys.stdin.readline().split()#入力待ち エンターが押されると，次にいく
			if len(input_lines) == 2:
				input_1 = input_lines[0]
				input_2 = input_lines[1]
				n_list = [str(i) for i in range(8)]
				if input_1 in kihu_dict:
					if input_2 in n_list:
						print kihu_dict[input_1],input_2
						break
					else:
						print 'retry'
				else:
					print 'retry'
			else:
				print 'retry'

	print "%s %s" % ("O" * board.count(1), "X" * board.count(2))


def main():
	play_othello()

if __name__ == '__main__':
	main()