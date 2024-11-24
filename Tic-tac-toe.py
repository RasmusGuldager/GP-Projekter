import sys

optagetFelter = []
player1 = {"felter": [], "markør": "X", "navn": "player1"}
player2 = {"felter": [], "markør": "O", "navn": "player2"}
træk = ""
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
currPlayer = 1
winning_combinations = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Column 1
        [1, 4, 7],  # Column 2
        [2, 5, 8],  # Column 3
        [0, 4, 8],  # Diagonal 1
        [2, 4, 6]   # Diagonal 2
    ]

def move(player):
    global currPlayer
    try:
        træk = input(player["navn"] + "'s tur: ")
        if int(træk) <= 9 and int(træk) >= 1 and int(træk) not in optagetFelter:
            optagetFelter.append(int(træk))
            board[int(træk)-1] = player["markør"]
            player["felter"].append(træk)
            if currPlayer == 1:
                currPlayer = 2
            else: currPlayer = 1
            checkForWinner()
            drawBoard()
        elif int(træk) < 1 or int(træk) > 9:
            print("Tallet skal være mellem 1 og 9!")
            if currPlayer == 1:
                move(player1)
            else: move(player2)
        else: 
            print("Feltet er optaget")
            if currPlayer == 1:
                move(player1)
            else: move(player2)
    except: 
        print("Forkert input")
        if currPlayer == 1:
                move(player1)
        else: move(player2)


def drawBoard():
    print(f'\n\n\n{player1["navn"]} = X\n{player2["navn"]} = O\n')
    print(f"{board[0]} | {board[1]} | {board[2]}\n---------\n{board[3]} | {board[4]} | {board[5]}\n---------\n{board[6]} | {board[7]} | {board[8]}\n")
    if currPlayer == 1:
        move(player1)
    else: move(player2)

def checkForWinner():
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]]:
            winner = board[combination[0]]
            if winner == player1["markør"]:
                print(f"\n\n\n{board[0]} | {board[1]} | {board[2]}\n---------\n{board[3]} | {board[4]} | {board[5]}\n---------\n{board[6]} | {board[7]} | {board[8]}\n")
                print("Vinderen er " + player1["navn"] + "\n\n\n")
                sys.exit(0)
            else:
                print(f"\n\n\n{board[0]} | {board[1]} | {board[2]}\n---------\n{board[3]} | {board[4]} | {board[5]}\n---------\n{board[6]} | {board[7]} | {board[8]}\n")
                print("Vinderen er " + player2["navn"] + "\n\n\n")
                sys.exit(0)

    if len(optagetFelter) == 9:
        print(f"\n\n\n{board[0]} | {board[1]} | {board[2]}\n---------\n{board[3]} | {board[4]} | {board[5]}\n---------\n{board[6]} | {board[7]} | {board[8]}\n")
        print("Spillet er uafgjort!\n\n\n")
        sys.exit(0)


player1["navn"] = input("Player1 navn: ")
player2["navn"] = input("Player2 navn: ")

drawBoard()
move(player1)