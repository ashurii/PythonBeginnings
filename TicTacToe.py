__author__ = 'Ashly Altman'

#   Board:
#   Create 3x3 grid. in first and second column of
#   first and second row print "_|", third column
#   print "_", and first and second of 3rd row print " |" and " " for final
#   space
#
#   Turn:
#   turn variable is set to X or O. If gameover == false,
#   Player is asked to enter numbers
#   for col and row. The turn character, X or O, is then added to the
#   corresponding board position. Then, if turn = X, turn becomes O,
#   or O becomes X
#
#   Win game:
#   initialize gameover = false
#   if    [0,0] == [0,1] == [0,2]
#   or  [1,0] == [1,1] == [1,1]
#   or  [2,0] == [2,1] == [2,2]
#   or  [0,0] == [1,0] == [2,0]
#   or  [0,1] == [1,1] == [2,1]
#   or  [0,2] == [1,2] == [2,2]
#   or  [0,0] == [1,1] == [2,2]
#   or  [0,2] == [1,1] == [2,0]
#   gameover = true. Print (turn " is the winner!")

print("Welcome to TicTacToe!")


#   // BOARD //


r, c = 3, 3
board = [[0 for x in range(r)] for y in range(c)]

for j in range(r):
    for i in range(c):
        board[j][i] = " |"

for j in range(r):
    print(board[j])
    for i in range(c):
        print(board[j][i], end="")


turn = 'X'
gameover = False
row = 0
col = 0

def checkforwin(board):
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        gameover = True
        print(turn, " is the winner!")
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' or board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        gameover = True
        print(turn, " is the winner!")
    elif board[2][0] == 'X' and board[2][0] == board[2][1] and board[2][1] == board[2][2] or board[2][0] == 'O' and board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        gameover = True
        print(turn, " is the winner!")
    elif board[0][0] == 'X' and board[0][0] == board[1][0] and board[1][0] == board[2][0] or board[0][0] == 'O' and board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        gameover = True
        print(turn, " is the winner!")
    elif board[0][1] == 'X' and board[0][1] == board[1][1] and board[1][1] == board[2][1] or board[0][1] == 'O' and board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        gameover = True
        print(turn, " is the winner!")
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        gameover = True
        print(turn, " is the winner!")
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        gameover = True
        print(turn, " is the winner!")
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        gameover = True
        print(turn, " is the winner!")
    else:
        gameover = False

# //PLAY//
print("player ", turn, " enter row and column: ")

while gameover == False:
    row = input("row: ")
    col = input("col: ")
    board[0][0] = turn
    checkforwin(board)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'




