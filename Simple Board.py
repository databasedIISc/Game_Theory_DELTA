def best_move(board):
    #TODO: Add a working code to play best move
    #return a string of 2 characters each from 0 to 2

    #Bad algorithm:
    for i in range(3):
        for j in range(3):
            if board[i][j]=="_":
                return str(i)+str(j)
def check(board,turn):
    #TODO: Check for win, loss or draw
    pass
print("Welcome to Tic Tac Toe!")
print("This is a 3x3 board. Enter the coordinates of the square you want to place your X or O in.")
print("The first player to get three in a row wins!")
print("The board is numbered like this:")
print("00 01 02")
print("10 11 12")
print("20 21 22")
print("Have fun!")
print(" ")
print(" ")
print(" ")
board=[["_","_","_"],["_","_","_"],["_","_","_"]]
turn=0
broke=False
while True:
    if turn==0:
        n=input("Your move:")
        while True:
            if n!="quit":
                if board[int(n[0])][int(n[1])]!="_":
                    print("That space is already taken!")
                    n=input("Your move:")
                else:    
                    board[int(n[0])][int(n[1])]="o"
                    break
            else:
                broke=True
                break
    elif turn==1:
        move=best_move(board)
        board[int(move[0])][int(move[1])]="x"
    if broke:
        break
    turn=1-turn
    print(" _ _ _")
    for i in range(3):
        print("|",end="")
        for j in range(3):
            print(board[i][j],end="|")
        print(" ")
    check(board,turn)
