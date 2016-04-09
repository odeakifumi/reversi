#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from random import randint

N = 8
SQUARE_TYPE=('.', 'O', 'X') #変更できないリスト 何もないときには０ドットで表す。
kihu_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}


def display_board(board):
	print '  a b c d e f g h'
	for i in xrange(N):
		print i,
		for j in xrange(N):
			print SQUARE_TYPE[board[i][j]],
		print
	print


def is_legal_move(board, me, opp, x, y):
	print me,opp,board
	if board[x][y] != 0:  # 既に駒が存在
		print "既に駒が存在"
		return False
	cand = [] #着手可能な手の候補をリストにする。
	# scan all directions
	for xx, yy in ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)): #縦、横、上、下、斜めの、８方向に打てるかどうかを確かめる。
		cand_tmp = [] #ひっくり返すことができるものをリストに代入する。
		distance = 1
		while True:
			xt = x + xx * distance 
			yt = y + yy * distance
			if xt >= N or xt < 0 or yt >= N or yt < 0: #端っこに到達したら中断する
				print"端っこに到達"
				break
			if board[xt][yt] == opp:     #調べる場所にに敵のコマがいるかを調べる。
				cand_tmp.append((xt, yt))#ここでひっくり返すことができそうなものをリストに代入する.
				distance += 1
				continue
			if board[xt][yt] == me and cand_tmp:#自分のコマとの間に敵のコマがあれば実行する。
				cand.extend(cand_tmp)           #確実にひっくり返すことができるならば、ここでcandに、cand_tmpを連結する.
				print "確実にひっくり返せる"
				break
			print "どのif文にも当てはまらない" 
			break	
	if not cand: #candが受け取っているリストがらだったら。
		print "candが受け取っているリストがらだった"
		return False
	else:
		return True 


def think_choice(board, me, opp):
	choice, result = None, []
	# for pos in xrange(64):
	for x in xrange(N):
		for y in xrange(N):
			if board[x][y] != 0:  # 既に駒が存在
				continue #55行目まで跳ばす
			cand = []
			# scan all directions
			for xx, yy in ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)): #縦、横、上、下、斜めの、８方向に打てるかどうかを確かめる。
				cand_tmp = []
				distance = 1
				while True:
					xt = x + xx * distance 
					yt = y + yy * distance
					if xt >= N or xt < 0 or yt >= N or yt < 0: #端っこに到達したら中断する
						break
					if board[xt][yt] == opp:     #盤上に敵のコマがいるか見方のコマがあるかによって、コマを置けるか置けないかを調べる。
						cand_tmp.append((xt, yt))#ここでひっくり返すことができそうなものをリストに代入する.
						distance += 1
						continue
					if board[xt][yt] == me and cand_tmp:#自分のコマとの間に敵のコマがあれば実行する。
						cand.extend(cand_tmp)           #確実にひっくり返すことができるならば、ここでcandに、cand_tmpを連結する。
						break
					break

				if not cand:
					continue
				# print xt, yt, cand, cand_tmp
				# nearly random strategy :)
				if (x, y) in ((0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1)): #着手可能な手の中で一番いい手を探す
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
	while True:
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
		is_legal = is_legal_move(board,player1,player2,kihu_dict[input_1],int(input_2))
		print is_legal
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
	print "%s %s" % ("O" * board.count(1), "X" * board.count(2))


def main():
	play_othello()

if __name__ == '__main__':
	main()