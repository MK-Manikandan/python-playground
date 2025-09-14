from os import system
from time import sleep
import random

#to clear the screen
def clear():
    _ = system('cls')
clear()

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
else:
    if random.randint(1, 2) == 1:
        choice = 'ba'
        print('Computer chose batting')
    else:
        choice = 'bo'
        print('Computer chose bowling')