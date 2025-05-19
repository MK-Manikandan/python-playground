print("╔═════════════════╗")
print("║  TIC TAC TOE 🕹 ║")
print("╚═════════════════╝")

#board dictionary
board={
    "tl": " ", "t": " ", "tr": " ",
    "ml": " ", "m": " ", "mr": " ",
    "bl": " ", "b": " ", "br": " "
    }

#printing out sample board with position
print("\nPosition names:")
print("╔═══╦═══╦═══╗")
print(f"║tl ║ t ║ tr║")
print("╠═══╬═══╬═══╣")
print(f"║ml ║ m ║ mr║")
print("╠═══╬═══╬═══╣")
print(f"║bl ║ b ║ br║")
print("╚═══╩═══╩═══╝")
print("tl:top left\tt:top   \ttr:top right\n\
ml:middle left\tm:middle\tmr:middle right\n\
bl:bottom left\tb:bottom\tbr:bottom right\n\n")

#function to print out the board
def display_board():
    print("╔═══╦═══╦═══╗")
    print(f"║ {board["tl"]} ║ {board["t"]} ║ {board["tr"]} ║")
    print("╠═══╬═══╬═══╣")
    print(f"║ {board["ml"]} ║ {board["m"]} ║ {board["mr"]} ║")
    print("╠═══╬═══╬═══╣")
    print(f"║ {board["bl"]} ║ {board["b"]} ║ {board["br"]} ║")
    print("╚═══╩═══╩═══╝")

turn = "X"
for i in range(9):
    while True:
        inp=input(f"{turn}\'s turn.\nEnter your position:")
        if inp not in board.keys():
            print(f"Wrong input. Enter any of these.\n{list(board.keys())}")
            continue
        else:
            break
    board[inp]=turn
    display_board()
    if turn == "X":
        turn = "O"
    else:
        turn = "X"



"""
Updates to do
--find a good output method or make it look good
--make rules
--add rule such that value cannot be entered in the same cell twice
--make input error handling------done
--use os module to update the same page instead of entering in new line
"""
