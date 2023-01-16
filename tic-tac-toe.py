board = ["-"]*9
player = "X"
game = True
win = None

def printboard(board):
    print(" "+board[0]+" "+"|"+" "+board[1]+" "+"|"+" "+board[2]+" ")
    print("____________")
    print(" " + board[3] + " " + "|"+" " + board[4] + " " + "|"+" " + board[5] + " ")
    print("____________")
    print(" " + board[6] + " " + "|"+" " + board[7] + " " + "|"+" " + board[8] + " ")

def playerinput(board):
    inp = int(input("enter a position 1-9 :"))
    if inp >= 1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = player
    else:
        print("the other player have already this position")
def playerswitch():
        global player
        if player == "X":
            player = "O"
        else:
            player ="X"
def gameconditionrow(board):
    global win
    global game
    if board[0]== board[1] == board[2] and board[1] != "-":
        win = board[0]
        return True
    elif board[3]== board[4] == board[5] and board[3] != "-":
        win = board[3]
        return True
    elif board[6]== board[7] == board[8] and board[6] != "-":
        win = board[6]
        return True
def gameconditioncollum(board):
    global win
    global game
    if board[0]== board[3] == board[6] and board[0] != "-":
        win = board[0]
        return True
    elif board[1]== board[4] == board[7] and board[1] != "-":
        win = board[1]
        return True
    elif board[2]== board[5] == board[8] and board[2] != "-":
        win = board[2]
        return True
def gameconditiondiag(board):
    global win
    global game
    if board[0] == board[4] == board[8] and board[0] != "-":
        win = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        win = board[2]
        return True

def checkwin():
    global game
    global win
    if gameconditionrow(board) or gameconditiondiag(board) or gameconditioncollum(board):
        printboard(board)
        print(win+" is the winner")
        game = False
def gametie(board):
    global game
    if "-" not in board:
        printboard(board)
        print("it's a tie ")
        game = False



while game:
    printboard(board)
    playerinput(board)
    gameconditionrow(board)
    gameconditiondiag(board)
    gameconditioncollum(board)
    gametie(board)
    playerswitch()
    checkwin()