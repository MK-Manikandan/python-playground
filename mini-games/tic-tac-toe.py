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
print(f"\t║ 1 ║ 2 ║ 3 ║")
print("\t╠═══╬═══╬═══╣")
print(f"\t║ 4 ║ 5 ║ 6 ║")
print("\t╠═══╬═══╬═══╣")
print(f"\t║ 7 ║ 8 ║ 9 ║")
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

#Main loop
turn = "X"
for i in range(9):
    _=os.system("cls" if os.name=="nt" else "clear")

    display_board()
    while True:
        inp=input(f"Current turn: {turn}.\nEnter your position:")
        if inp not in board.keys():
            print(f"\nWrong input. Enter a correct position name.\n")
            continue
        else:
            break
    board[inp]=turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
os.system("pause")

"""
Updates to do
--make rules
--add rule such that value cannot be entered in the same cell twice
"""
