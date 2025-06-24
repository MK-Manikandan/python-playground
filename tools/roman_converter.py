def check_if_num(i):
    try:
        i=int(i)
        return i
    except:
        return False

def num_to_rom(j):
    output=''
    roman_dict={
        'M': 1000, 'CM': 900, 'D':500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }
    for key, value in roman_dict.items():
        quo = int(j/value)
        j-=quo*value
        output += (quo*key)
    return output

def rom_to_num(k):
    pass

while True:
    inp = input("Enter the input: ")
    if inp == "0":
        break
    if check_if_num(inp):
        if int(inp)>3999:
            print('The largest number standard Roman Numerals can represent is 3999\n')
            continue
        print(f'Output: {num_to_rom(int(inp))}')
    else:
        print(f'Output: {rom_to_num(inp)}')