# to check if the entered input is number or roman numeral
def check_if_num(i):
    try:
        i=int(i)
        return i
    except:
        return False
    
# check if it is a valid roman numeral
def check_if_roman(m):
    roman=['I', 'V', 'X', 'L', 'C', 'D', 'M']
    for i in m:
        if i not in roman:
            return False
    return True

# converting number to roman numeral
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

# converting roman numeral to number
def rom_to_num(k):
    roman_dict={
        'M': 1000, 'D':500, 'C': 100, 'L': 50,
        'X': 10, 'V': 5, 'I': 1
    }  
    output=0
    lastnum=0
    k = k[::-1]
    for l in k:
        if roman_dict[l] < lastnum:
            output-=roman_dict[l]
        else:
            output+=roman_dict[l]
            lastnum=roman_dict[l]
    return output

#Header
print('\n╔═══════════════════════════╗')
print('║  Roman numeral converter  ║')
print('╚═══════════════════════════╝')
print('\n-Enter number to convert to roman numeral\n-Enter roman numeral to convert to number\n-Enter zero to end the program\n')

# input and output loop
while True:
    inp = input("Enter the input: ")
    if inp == "0":
        break
    if check_if_num(inp):
        if int(inp)>3999:
            print('The largest number standard Roman Numerals can represent is 3999\n')
            continue
        print(f'Output: {num_to_rom(int(inp))}\n')
    else:
        if not check_if_roman(inp.upper()):
            print('Invalid input\n')
            continue
        print(f'Output: {rom_to_num(inp.upper())}\n')

'''
    Manikandan M
    manikantanm07mk@gmail.com
    https://github.com/MK-Manikandan
    https://www.linkedin.com/in/manikandan--m
    24th June 2025
'''