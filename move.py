#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
import sys

from config import *


def is_legal_move(board, me, opp, x, y):
	if board[x][y] != 0:  # 既に駒が存在
		return False, None
	cand = [] #着手可能な手の候補をリストにする。
	# scan all directions
	for xx, yy in ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)): #縦、横、上、下、斜めの、８方向に打てるかどうかを確かめる。
		cand_tmp = [] #ひっくり返すことができるものをリストに代入する。
		distance = 1
		while True:
			xt = x + xx * distance 
			yt = y + yy * distance
			if xt >= N or xt < 0 or yt >= N or yt < 0: #端っこに到達したら中断する
				break
			if board[xt][yt] == opp:     #調べる場所にに敵のコマがいるかを調べる
				cand_tmp.append((xt, yt))#ここでひっくり返すことができそうなものをリストに代入する
				distance += 1
				continue
			if board[xt][yt] == me and cand_tmp:#自分のコマとの間に敵のコマがあれば実行する。
				cand.extend(cand_tmp)           #確実にひっくり返すことができるならば、ここでcandに、cand_tmpを連結する
				break
			break	
	if not cand: #candが受け取っているリストがらだったら
		return False, None
	else:
		return True, cand


def cpu_choice(board, me, opp):
	choice, result = None, []
	# for pos in xrange(64):
	for x in xrange(N):
		for y in xrange(N):
			if board[x][y] != 0:  # 既に駒が存在
				continue #55行目まで跳ばす
			cand = []
			# scan all directions
			for xx, yy in ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)): #縦、横、上、下、斜めの、８方向に打てるかどうかを確かめる
				cand_tmp = []
				distance = 1
				while True:
					xt = x + xx * distance 
					yt = y + yy * distance
					if xt >= N or xt < 0 or yt >= N or yt < 0: #端っこに到達したら中断する
						break
					if board[xt][yt] == opp:     #盤上に敵のコマがいるか見方のコマがあるかによって、コマを置けるか置けないかを調べる
						cand_tmp.append((xt, yt))#ここでひっくり返すことができそうなものをリストに代入する
						distance += 1
						continue
					if board[xt][yt] == me and cand_tmp:#自分のコマとの間に敵のコマがあれば実行する
						cand.extend(cand_tmp)           #確実にひっくり返すことができるならば、ここでcandに、cand_tmpを連結する
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


def user_choice(board, me, opp):
	while True:
		input_lines = sys.stdin.readline().split()#入力待ち エンターが押されると，次にいく
		if len(input_lines) == 2:
			input_1 = input_lines[0]
			input_2 = input_lines[1]
			n_list = [str(i) for i in range(8)]
			if input_1 in KIFU_DICT:
				if input_2 in n_list:
					print KIFU_DICT[input_1],input_2
					is_legal, cand = is_legal_move(board, me, opp, x=int(input_2), y=KIFU_DICT[input_1])
					if is_legal:
						break
				else:
					print 'retry'
			else:
				print 'retry'
		else:
			print 'retry'
	return (int(input_2), KIFU_DICT[input_1]), cand