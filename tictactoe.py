
#checks the board to see if anyone has won, or if there is a draw. 
def threeInARow(row1, col1, row2, col2, row3, col3, board):
  if board[row1][col1] == board[row2][col2]==board[row3][col3] !=0:
    return board[row1][col1]
  return 0
  
  
def didAnyoneWin(board):
  for i in range(0, 3):
    possibleWin = threeInARow(i,0,i,1,i,2,board)
    if possibleWin:
      return possibleWin
    possibleWin = threeInARow(0,i,1,i,2,i,board)
    if possibleWin:
      return possibleWin
  diagonal1 = threeInARow(0,0,1,1,2,2,board)
  if diagonal1:
    return diagonal1
  diagonal2 = threeInARow(2,0,1,1,0,2,board)
  if diagonal2:
    return diagonal2
  return 0

def validateMove(board, row, col, turn):
  if row < 0 or row > 2 or col < 0 or col > 2:
    print("Those coordinates don't correspond to a space in the board")
    print("that was not a valid move. try again")
    return False
  if board[row][col] != 0:
    print("That space is already full")
    print("that was not a valid move. try again")
    return False
  return True

def printBoard(board):
  for row in board:
    toPrint = "|"
    for i in range(0,3):
      if row[i] == 1:
        toPrint+="X|"
      elif row[i] == -1:
        toPrint+="O|"
      else:
        toPrint+=" |"
    print(toPrint)
    
  

def gameloop(board, winner, turn):
    validMove = False
    while not validMove:
      try:
        row = int(input("enter the row (0 = top, 1 = mid, 2 = bottom)"))
        col = int(input("enter the col (0 = left, 1 = mid, 2 = right)"))
        validMove = validateMove(board, row, col, turn)
      except ValueError:
        print("you entered something other than an int. Don't do that!")
    board[row][col] = turn
    printBoard(board)
    winner = didAnyoneWin(board)
    return (board, winner, (turn*-1))


def main():
    board = [[0,0,0],[0,0,0],[0,0,0]]
    winner = 0 #If player 1 wins, winner=1. If player 2 wins, winner=-1 (confusing, I know), if not yet finished, winner=0. If the numTurns counter reaches 9 without anyone winning, then we have a draw.
    numTurns = 0
    turn = 1 #turn = 1 for player 1's turn. turn=-1 for player 2's turn
    while(winner==0 and numTurns < 9):
        (board, winner, turn) = gameloop(board, winner, turn)
        numTurns+=1 
    if winner==1:
        print("THIS GAME'S WINNER IS: PLAYER ONE!")
    elif winner==-1:
        print("THIS GAME'S WINNER IS: PLAYER TWO!")
    else:
        print("IT'S A DRAW! AND WHAT A LOVELY DRAW IT IS!")
    return


main()
