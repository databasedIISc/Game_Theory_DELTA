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
while True:
    n=input("move:")
    if board[int(n[0])][int(n[1])]!="_":
        print("That space is already taken!")
        continue
    else:
        if turn==0:
            board[int(n[0])][int(n[1])]="o"
        else:
            board[int(n[0])][int(n[1])]="x"
        turn=1-turn
    print(" _ _ _")
    for i in range(3):
        print("|",end="")
        for j in range(3):
            print(board[i][j],end="|")
        print(" ")
