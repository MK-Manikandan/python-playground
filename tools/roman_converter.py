def check_if_num(i):
    try:
        int(i)
        return True
    except:
        return False

def num_to_rom(j):
    pass

def rom_to_num(k):
    pass

while True:
    inp = input("Enter the input: ")
    if inp == "0":
        break
    if check_if_num(inp):
        print(f'Output: {num_to_rom(inp)}')
    else:
        print(f'Output: {rom_to_num(inp)}')
