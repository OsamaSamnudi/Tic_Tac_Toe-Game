# Show Board:
def ShowBoard(Board):
    for row in Board:
        for col in row:
            print(col, end="\t")
        print("\n")

# Set Player:


def Set_Player():
    from random import choice
    Player1 = choice(['X', 'Z'])
    if Player1 == 'Z':
        Player2 = 'X'
    else:
        Player2 = "Z"
    return Player1, Player2

# Take Input:


def Play_Input(Board, Player):
    while True:
        Playing_range = range(1, 10)
        Player_Input = input("Please select a num for 1 to 9 : ")
        if str(Player_Input) in Playing_range:
            print("You have to select ((( from 1 to 9)))")
            continue
        if Player_Input == "1" and Board[0][0].isdigit():
            Board[0][0] = Player
            break
        elif Player_Input == "2" and Board[0][1].isdigit():
            Board[0][1] = Player
            break
        elif Player_Input == "3" and Board[0][2].isdigit():
            Board[0][2] = Player
            break
        elif Player_Input == "4" and Board[1][0].isdigit():
            Board[1][0] = Player
            break
        elif Player_Input == "5" and Board[1][1].isdigit():
            Board[1][1] = Player
            break
        elif Player_Input == "6" and Board[1][2].isdigit():
            Board[1][2] = Player
            break
        elif Player_Input == "7" and Board[2][0].isdigit():
            Board[2][0] = Player
            break
        elif Player_Input == "8" and Board[2][1].isdigit():
            Board[2][1] = Player
            break
        elif Player_Input == "9" and Board[2][2].isdigit():
            Board[2][2] = Player
            break
        else:
            print("Invalid : select (((from 1 to 9))) ")
        continue
    ShowBoard(Board)

# Check Full Board:


def Check_Full_Board(Board):
    Empty_Board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    NewBoard = Board[0]+Board[1]+Board[2]
    NewBoard
    Digits = 0
    for S in NewBoard:
        if S in Empty_Board:
            Digits = Digits+1
    if Digits == 0:
        Check = True  # (False = all cells has X or O)
    else:
        Check = False  # (True = some cells still empty)
    return Check

# Check Winner:


def Check_Winner(Board):
    return Board[0][0] == Board[0][1] == Board[0][2] or\
        Board[1][0] == Board[1][1] == Board[1][2] or\
        Board[2][0] == Board[2][1] == Board[2][2] or\
        Board[0][0] == Board[1][1] == Board[2][2] or\
        Board[0][2] == Board[1][1] == Board[2][0]

# Lets_Play


def Play():
    Player1, Player2 = Set_Player()
    print("Player1 :  ", Player1)
    print("Player2 :  ", Player2)
    B = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    ShowBoard(B)
    while True:
        for Player in [Player1, Player2]:
            print(f"{Player} turn")
            Play_Input(B, Player)
            print("------------------")
            if Check_Winner(B):
                print(f"{Player} Is WINNER")
                break
            if Check_Full_Board(B):
                print("Game Over")
                break
        if Check_Winner(B):
            break
        if Check_Full_Board(B):
            break


Play()
