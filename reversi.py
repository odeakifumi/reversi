import sys
from random import randint


def display_board(board):
    for i in xrange(8):
        for j in board[i * 8:i * 8 + 8]:
            print('.', 'O', 'X')[j],
        print
    print


def think_choice(board, me, opp):
    choice, result = None, []
    for pos in xrange(64):
        if board[pos] != 0:
          continue
        x = pos % 8
        y = pos / 8
        cand = []
        # scan all directions
        for xx, yy in ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)):
            cand_tmp = []
            distance = 1
            while True:
                xt = x + xx * distance
                yt = y + yy * distance
                if xt > 7 or xt < 0 or yt > 7 or yt < 0:
                    break
                p = yt * 8 + xt
                if board[p] == opp:  #add candidate
                    cand_tmp.append(p)
                    distance += 1
                    continue
                if board[p] == me and cand_tmp:  #fix candidate
                    cand.extend(cand_tmp)
                    break
                break
            if not cand:
                continue
            # nearly random strategy :)
            if pos in (0, 7, 56, 63):
                return pos, cand  # sumikko!
            if len(cand) + randint(0, 1) > len(result):
                choice, result = pos, cand
    return choice, result


def play_othello():
    board = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 1, 2, 0, 0, 0,
    0, 0, 0, 2, 1, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    ]
    display_board(board)
    player1, player2 = 1, 2
    r = []
    while 1:
        choice, result = think_choice(board, me=player1, opp=player2)
        if result:
            board[choice] = player1
            for i in result:
              board[i] = player1
        if not (r or result):
          break
        r = result
        display_board(board)
        player1, player2 = player2, player1
        sys.stdin.readline()
    print "%s %s" % ("O" * board.count(1), "X" * board.count(2))

while 1:
  play_othello()