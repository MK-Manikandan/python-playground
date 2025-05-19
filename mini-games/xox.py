board={
    'tl': ' ', 't': ' ', 'tr': ' ',
    'ml': ' ', 'm': ' ', 'mr': ' ',
    'bl': ' ', 'b': ' ', 'br': ' '
    }

#function to print out the board
def display_board():
    print(board['tl']+'|'+board['t']+'|'+board['tr'])
    print('-+-+-')
    print(board['ml']+'|'+board['m']+'|'+board['mr'])
    print('-+-+-')
    print(board['bl']+'|'+board['b']+'|'+board['br'])

display_board()

turn = 'X'
for i in range(9):
    inp=input(f'{turn}\'s turn.\nEnter your position:')
    board[inp]=turn
    display_board()
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'



'''
Updates to do
--find a good output method or make it look good
--make rules
--make input error handling
'''
