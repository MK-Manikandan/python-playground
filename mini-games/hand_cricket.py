from os import system
from time import sleep
import random
import platform
import sys

#to clear the screen
def clear():
    if platform.system() == 'Windows':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

#Header
def header():
    print('\n╔══════════════════════╗')
    print('║     Hand Cricket     ║')
    print('╚══════════════════════╝\n')
header()

#Starting the game
overs = 6
wickets = 6
print('Play - 1\nCustomize and play - 2')
while True:
    try:
        game = int(input('Enter the choice: '))
    except Exception:
        print('Enter a valid input (1 or 2)')
        continue
    if game in [1, 2]:
        break
    else:
        print('Wrong input!!!  Try again.')
if game == 1:
    pass
elif game == 2:
    while True:
        try:
            overs = int(input('Enter number of overs: '))
        except Exception:
            print('Enter a valid input (number)')
            continue
        if overs < 1:
            print('Enter a positive integer')
            continue
        break
    while True:
        try:
            wickets = int(input('Enter number of wickets: '))
        except Exception:
            print('Enter a valid input (number)')
            continue
        if overs < 1:
            print('Enter a positive integer')
            continue
        break
    

#tossing the coin
coin = ['h', 't']
print('Head or Tail')
while True:
    choice = input('Enter h/t : ')
    if choice.lower() in coin:
        break
    else:
        print('Wrong input!!! Try again.')
toss = random.choice(coin)
print('Tossing the coin', end = '', flush = True)
sleep(0.5)
print('.', end = '', flush = True)
sleep(0.5)
print('.', end = '', flush = True)
sleep(0.5)
print('.', end = '', flush = True)
sleep(0.5)
print(f'\nToss = {toss}')
sleep(0.5)
if choice.lower() == toss:
    print('You got the toss')
    toss = True
else:
    print('You lost the toss')
    toss = False
sleep(0.7)
#choosing batting or bowling
if toss:
    while True:
        choice = input('\nChoose batting or bowling (ba/bo): ')
        if choice.lower() in ['ba', 'bo']:
            break
        else:
            print('Wrong input!!!  Try again.')
    if choice == 'ba':
        print('You chose batting')
    else:
        print('You chose bowling')
else:
    #choosing reverse here because computer's batting is player's bowling
    if random.randint(1, 2) == 1:
        choice = 'bo'
        print('Computer chose batting')
    else:
        choice = 'ba'
        print('Computer chose bowling')
system('pause')

#One over for both bowling and batting
def over(runs, what):
    for i in range(1, 7):
        global wickets_left
        if runs < 0:
            if choice == 'ba':
                result(False)
            else:
                result(True)
        if what == 'first_innings':
            print(f'\nRuns : {runs}')
        else:
            print(f'\nRuns left to win : {runs + 1}')
        print(f'---Ball {i}---')
        while True:
            try:
                player = int(input('Your choice: '))
            except Exception:
                print('Enter a valid input ( a number in 1 - 6)')
                continue
            if player in range(7):
                break
            else:
                print('Wrong input!!!  Try again.')
        computer = random.randint(0, 6)
        print(f'Computer\'s choice : {computer}')
        sleep(0.5)
        if player == computer:
            print('\nOut')
            wickets_left -= 1
            if wickets_left == 0:
                return runs
            print(f'(Wickets left : {wickets_left})')
        else:
            if (what == 'first_innings' and choice == 'ba'):
                runs += player
            elif (what == 'first_innings' and choice == 'bo'):
                runs += computer
            elif (what == 'second_innings' and choice == 'ba'):
                runs -= computer
            else:
                runs -= player
    return runs

def result(a):
    if a:
        print('Congratulations. You have won')
        system('pause')
        sys.exit()
    else:
        print('Sorry, You have lost')
        system('pause')
        sys.exit()

#Main game loop
player_runs = 0

for j in range(2):
    global wickets_left
    wickets_left = wickets
    clear()
    header()
    if (j == 0 and choice == 'ba') or (j == 1 and choice == 'bo'):
        print('\n__..-- Your Batting --..__')
    else:
        print('\n__..-- Your Bowling --..__')
    if j == 1:
        print(f'\nRuns to win : {player_runs + 1}')
    for i in range(overs):
        print(f'\n     Over {i + 1}   (Wickets left : {wickets_left})\n-------------------------------------')
        if j == 0:
            player_runs = over(player_runs, 'first_innings')
        else:
            player_runs = over(player_runs, 'second_innings')
        if wickets_left == 0:
            break
    print('----Innings over----')
    system('pause')
if choice == 'ba':
    result(True)
else:
    result(False)