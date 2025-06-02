import os
_=os.system("cls" if os.name=="nt" else "clear")

#game header
print("\t╔═════════════════╗")
print("\t║   TIC TAC TOE   ║")
print("\t╚═════════════════╝")

#board dictionary
board={
    "1": " ", "2": " ", "3": " ",
    "4": " ", "5": " ", "6": " ",
    "7": " ", "8": " ", "9": " "
    }

#Printing out the sample board with position name
print("\nPosition names:")
print("\t╔═══╦═══╦═══╗")
print("\t║ 1 ║ 2 ║ 3 ║")
print("\t╠═══╬═══╬═══╣")
print("\t║ 4 ║ 5 ║ 6 ║")
print("\t╠═══╬═══╬═══╣")
print("\t║ 7 ║ 8 ║ 9 ║")
print("\t╚═══╩═══╩═══╝")
os.system("pause")

#function to print out the board
def display_board():
    print("\tSample Board\t Main Board")
    print("\t╔═══╦═══╦═══╗\t╔═══╦═══╦═══╗")
    print(f"\t║ 1 ║ 2 ║ 3 ║\t║ {board["1"]} ║ {board["2"]} ║ {board["3"]} ║")
    print("\t╠═══╬═══╬═══╣\t╠═══╬═══╬═══╣")
    print(f"\t║ 4 ║ 5 ║ 6 ║\t║ {board["4"]} ║ {board["5"]} ║ {board["6"]} ║")
    print("\t╠═══╬═══╬═══╣\t╠═══╬═══╬═══╣")
    print(f"\t║ 7 ║ 8 ║ 9 ║\t║ {board["7"]} ║ {board["8"]} ║ {board["9"]} ║")
    print("\t╚═══╩═══╩═══╝\t╚═══╩═══╩═══╝")

#Game rules

#dictionary containing the names of rows, columns and diagonals
check_dict={
    "row1" : ["1", "2", "3"], "row2" : ["4", "5", "6"], "row3" : ["7", "8", "9"],
    "col1" : ["1", "4", "7"], "col2" : ["2", "5", "8"], "col3" : ["3", "6", "9"],
    "dia1" : ["1", "5", "9"], "dia2" : ["3", "5", "7"]
}

#function to check if any rows or columns or diagonals are equal
def check_if_equal(row_name):
    if (board[check_dict[row_name][0]] == board[check_dict[row_name][1]]) and (board[check_dict[row_name][0]] == board[check_dict[row_name][2]]):
        return True
    else:
        return False

#function to find which all row and column to check for
def check_dict_func(pos):
    for key, value in check_dict.items():
        if pos in value:
            decision = check_if_equal(key)
            if decision:
                return decision
        else:
            continue
    return False

#final function to run, if won
def won(turn):
    _=os.system("cls" if os.name=="nt" else "clear")
    display_board()
    print(f"\nCongratulations!!!\n{turn} have won\n")
    return True

#Main loop
turn = "X"
for i in range(9):
    _=os.system("cls" if os.name=="nt" else "clear")

    display_board()
    while True:
        inp=input(f"Current turn: {turn}.\nEnter your position:")
        if inp not in board.keys():
            print("\nWrong input. Enter a correct position name.")
            continue
        elif board[inp] != " ":
            print(f"\nPosition {inp} in board is not empty, enter an empty position.")
            continue
        else:
            break
    board[inp]=turn
    checking = check_dict_func(inp)
    finish = False
    if checking:
        finish = won(turn)
        break
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

#if nobody won
if not finish:
    _=os.system("cls" if os.name=="nt" else "clear")
    display_board()
    print("\nNobody won!!!\n")
os.system("pause")


"""
    Manikandan M
    manikantanm07mk@gmail.com
    https://github.com/MK-Manikandan
    https://www.linkedin.com/in/manikandan--m
    2nd June 2025
"""