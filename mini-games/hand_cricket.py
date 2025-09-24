from os import system
from time import sleep
import random
import platform
import sys

#function to clear the screen
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

#Starting the game with options to customize wickets and overs
overs = 6
wickets = 6
print('Start Playing(6 Overs, 6 Wickets) -> 1\nCustomize and play -> 2')
while True:
    try:
        game = int(input('\nEnter the choice: '))
    except Exception:
        print('!!!Enter a valid input (1 or 2)')
        continue
    if game in [1, 2]:
        break
    else:
        print('Wrong input!!!  Try again.')
if game == 1:
    pass
elif game == 2:
    print('\nYou can choose the number of overs and number of wickets')
    while True:
        try:
            overs = int(input('Enter number of overs: '))
        except Exception:
            print('!!!Enter a valid input (number)')
            continue
        if overs < 1:
            print('!!!Enter a positive integer')
            continue
        break
    while True:
        try:
            wickets = int(input('Enter number of wickets: '))
        except Exception:
            print('!!!Enter a valid input (number)')
            continue
        if overs < 1:
            print('!!!Enter a positive integer')
            continue
        break

#tossing the coin
print('\n-----Coint toss-----')
coin = ['h', 't']
print('Head or Tail')
while True:
    choice = input('Enter h/t : ')
    if choice.lower() in coin:
        break
    else:
        print('Wrong input!!! Try again.')
toss = random.choice(coin)
print('\nTossing the coin', end = '', flush = True)
sleep(0.5)
print('.', end = '', flush = True)
sleep(0.5)
print('.', end = '', flush = True)
sleep(0.5)
print('.', end = '', flush = True)
sleep(0.5)
print()
print(f'\nToss = {toss}')
sleep(0.8)
if choice.lower() == toss:
    print('\n------------------------'
          '\n**--You got the toss--**'
          '\n------------------------\n')
    toss = True
else:
    print('\n------------------------'
          '\n**--You lost the toss--**'
          '\n------------------------\n')
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
        print('**--You choose batting--**\n')
    else:
        print('**--You choose bowling--**\n')
else:
    #choosing reverse here because computer's batting is player's bowling
    if random.randint(1, 2) == 1:
        choice = 'bo'
        print('**--Computer choose batting--**\n')
    else:
        choice = 'ba'
        print('**--Computer choose bowling--**\n')
system('pause')

#One over for both bowling and batting
#Out mechanism is also added here
def over(runs, what):
    for i in range(1, 7):
        global wickets_left
        if runs < 0:
            print('\n---------Innings over---------\n')
            system('pause')
            if choice == 'ba':
                result(False)
            else:
                result(True)
        if what == 'first_innings':
            print(f'\n            Runs : {runs}')
        else:
            print(f'\nRuns left to win : {runs + 1}')
        print(f'-------Ball  {i}-------')
        while True:
            try:
                player = int(input('       Your choice: '))
            except Exception:
                print('Enter a valid input (0 - 6)')
                continue
            if player in range(7):
                break
            else:
                print('Wrong input!!!  Try again.')
        computer = random.randint(0, 6)
        print(f'Computer\'s choice : {computer}')
        sleep(0.7)
        if player == computer:
            print('\n-----------------------\n'
                  '****---   OUT   ---****'
                  '\n-----------------------')
            sleep(0.7)
            wickets_left -= 1
            if wickets_left == 0:
                return runs
            print(f'(Wickets left : {wickets_left})')
        else:
            if (what == 'first_innings' and choice == 'ba'):
                if player == 0:
                    runs += computer
                runs += player
            elif (what == 'first_innings' and choice == 'bo'):
                if computer == 0:
                    runs += player
                runs += computer
            elif (what == 'second_innings' and choice == 'ba'):
                if computer == 0:
                    runs -= player
                runs -= computer
            else:
                if player == 0:
                    runs -= computer
                runs -= player
    return runs

# winning or losing result interface
def result(a):
    clear()
    header()
    if a:
        print('\n******************************************'
              '\n***------------------------------------***'
              '\n***--- Congratulations You have won ---***'
              '\n***------------------------------------***'
              '\n******************************************\n')
        system('pause')
        sys.exit()
    else:
        print('\n***********************************'
              '\n***-----------------------------***'
              '\n***---  Sorry You have lost  ---***'
              '\n***-----------------------------***'
              '\n***********************************\n')
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
        print('\n    \\\\\\\\-- Your Batting --////')
    else:
        print('\n    \\\\\\\\-- Your Bowling --////')
    if j == 1:
        print(f'\nRuns to win : {player_runs + 1}')
    for i in range(overs):
        print('\n---------------------------------'
              f'\n     Over {i + 1}   (Wickets left : {wickets_left})'
              '\n---------------------------------')
        if j == 0:
            player_runs = over(player_runs, 'first_innings')
        else:
            player_runs = over(player_runs, 'second_innings')
        if wickets_left == 0:
            break
    print('\n---------Innings over---------\n')
    system('pause')

# deciding result
if choice == 'ba':
    result(True)
else:
    result(False)


"""
    Manikandan M
    manikantanm07mk@gmail.com
    https://github.com/MK-Manikandan
    https://www.linkedin.com/in/manikandan--m
    25th Septmber 2025
"""