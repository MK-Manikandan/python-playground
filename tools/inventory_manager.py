import json
try:
    with open('data.json', 'r') as file:
        inv=json.load(file)
except:
    inv=dict()

def dict_inp():
    print('Format: item_name<space>number\nEnter zero when finished\n')
    while True:
        inp=input()
        if inp=='0':
            break
        inp=inp.split(' ')
        inp[0]=inp[0].capitalize()
        try:
            inv[inp[0]]=inv.get(inp[0],0)+int(inp[1])
        except:
            print('Invalid input\n')
            continue

dict_inp()

with open('data.json', 'w') as file:
    json.dump(inv, file)