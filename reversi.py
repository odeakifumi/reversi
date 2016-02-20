#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from random import randint

N = 8


def display_board(board):
	for i in xrange(N):
		for j in xrange(N):
			print('.', 'O', 'X')[board[i][j]],
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
	# board = [
	# 0, 0, 0, 0, 0, 0, 0, 0,
	# 0, 0, 0, 0, 0, 0, 0, 0,
	# 0, 0, 0, 0, 0, 0, 0, 0,
	# 0, 0, 0, 1, 2, 0, 0, 0,
	# 0, 0, 0, 2, 1, 0, 0, 0,
	# 0, 0, 0, 0, 0, 0, 0, 0,
	# 0, 0, 0, 0, 0, 0, 0, 0,
	# 0, 0, 0, 0, 0, 0, 0, 0,
	# ]
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
		sys.stdin.readline()
	print "%s %s" % ("O" * board.count(1), "X" * board.count(2))


def main():
	play_othello()


if __name__ == '__main__':
	main()
