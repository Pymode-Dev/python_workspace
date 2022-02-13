# this is a tic_tac_toe program between two users


board = {'tl': ' ', 'tm': ' ', 'tr': ' ',
         'ml': ' ', 'mm': ' ', 'mr': ' ',
         'll': ' ', 'lm': ' ', 'lr': ' '
         }


def the_board(simulation):
    print(simulation['tl'] + '|' + simulation['tm'] + '|' + simulation['tr'])
    print('-+-+-')
    print(simulation['ml'] + '|' + simulation['mm'] + '|' + simulation['mr'])
    print('-+-+-')
    print(simulation['ll'] + '|' + simulation['lm'] + '|' + simulation['lr'])
    print('-+-+-')


the_board(board)

player1, player2 = 'x', 'o'
turn = player1
for i in range(9):
    the_board(board)
    print('The turn for', turn, 'to which space?:')
    move = input()  # the text must be among the simulated keys in board
    board[move] = turn
    if turn == player1:
        turn = player2
    else:
        turn = player1


def score_update():
    p1_score, p2_score = 0, 0
    if player1:
        if board['tl'] == board['tm'] == board['tr'] or \
           board['ml'] == board['mm'] == board['mr'] or \
           board['ll'] == board['lm'] == board['lr'] or \
           board['tl'] == board['mm'] == board['mr'] or \
           board['tr'] == board['mm'] == board['ml'] or \
           board['tm'] == board['mm'] == board['lm']:
            p1_score += 1
            print('player1 wins')
    elif player2:
        if board['tl'] == board['tm'] == board['tr'] or \
           board['ml'] == board['mm'] == board['mr'] or \
           board['ll'] == board['lm'] == board['lr'] or \
           board['tl'] == board['tm'] == board['tr'] or \
           board['tm'] == board['mm'] == board['lm']:
            pass
