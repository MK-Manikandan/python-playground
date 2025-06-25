import json

try:
    with open('data.json', 'r') as file:
        inv = json.load(file)
except:
    inv = dict()

def dict_inp():
    print('Format: item_name<space>number\nEnter zero when finished\n')
    while True:
        inp=input()
        if inp == '0':
            break
        inp = inp.split(' ')
        inp[0] = inp[0].capitalize()
        try:
            inv[inp[0]] = inv.get(inp[0],0)+int(inp[1])
        except:
            print('Invalid input\n')
            continue

def show():
    if len(inv)==0:
        print('The list is empty')
        return
    for k, v in inv.items():
        print(f'{k} : {v}')

def clear():
    global inv
    inv = dict()

while True:
    print('0 - stop the program\n1 - enter more items\
          \n2 - show the list\n3 - clear the list')
    decision = input()
    if decision == '0':
        break
    elif decision == '1':
        dict_inp()
    elif decision == '2':
        show()
    elif decision == '3':
        clear()
with open('data.json', 'w') as file:
    json.dump(inv, file)

#make a function for output
#last commit was save in to and load out of a file