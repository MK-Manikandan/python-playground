from os import system
from time import sleep
import random
import platform

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
    except:
        print('Enter a valid input (1 or 2)')
        continue
    if game in [1, 2]: break
    else: print('Wrong input!!!  Try again.')
if game == 1: pass
elif game == 2:
    while True:
        try:
            overs = int(input('Enter number of overs: '))
        except:
            print('Enter a valid input (number)')
            continue
        if overs < 1:
            print('Enter a positive integer')
            continue
        break
    while True:
        try:
            wickets = int(input('Enter number of wickets: '))
        except:
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
    if choice.lower() in ['h', 't']: break
    else: print('Wrong input!!! Try again.')
toss = random.choice(coin)
print('Tossing the coin', end = '')
sleep(0.3)
for i in range(3):
    print('.', end = '')
    sleep(0.3)
print(f'\nToss = {toss}')
sleep(0.5)
if choice.lower() == toss:
    print('You got the toss')
    toss = True
else:
    print('You lost the toss')
    toss = False
sleep(0.5)

#choosing batting or bowling
if toss:
    while True:
        choice = input('\nChoose batting or bowling (ba/bo): ')
        if choice.lower() in ['ba', 'bo']: break
        else: print('Wrong input!!!  Try again.')
    if choice == 'ba': print('You chose batting')
    else: print('You chose bowling')
    sleep(2)
else:
    #choosing reverse here because computer's batting is player's bowling
    if random.randint(1, 2) == 1:
        choice = 'bo'
        print('Computer chose batting')
    else:
        choice = 'ba'
        print('Computer chose bowling')
    sleep(2)

#One over for both bowling and batting
def over(runs, what):
    for i in range(1, 7):
        if runs < 0: result(False)
        if what == 'ba':
            print(f'\nRuns : {runs}')
        else:
            print(f'\nRuns left to win : {runs}')
        print(f'---Ball {i}---')
        while True:
            try:
                bat = int(input('Your choice: '))
            except:
                print('Enter a valid input ( a number in 1 - 6)')
                continue
            if bat in range(7): break
            else: print('Wrong input!!!  Try again.')
        ball = random.randint(0, 6)
        print(f'Computer\'s choice : {ball}')
        sleep(0.5)
        if bat == ball:
            print('Out')
            return runs, True
        else:
            if what == 'ba':
                runs += bat
            else:
                runs -= ball
    return runs, False

def result(a):
    if a:
        print('Congratulations. You have won')
        system('pause')
        quit()
    else:
        print('Sorry, You have lost')
        system('pause')
        quit()

#Main game loop
player_runs = 0
computer_runs = 0
#batting
if choice == 'ba':
    for j in range(2):
        wickets_left = wickets
        clear()
        header()
        if j == 0:
            print('\n⟬ Your Batting ⟭')
        else:
            print('\n⟬ Your Bowling ⟭')
        for i in range(overs):
            print(f'\n     Over {3}   (Wickets left : {3})\n-------------------------------------')
            if j == 0:
                player_runs, if_out = over(player_runs, 'ba')
            else:
                player_runs, if_out = over(player_runs, 'bo')
            if if_out:
                wickets_left -= 1
            if wickets_left == 0:
                print('Innings over')
                break
        print('----Innings over----')
print(f'Player = {player_runs}\nComputer = {computer_runs}')
