"""Before your interview, write a program that lets two humans play a game of Tic Tac Toe in a terminal.
The program should let the players take turns to input their moves. The program should report the outcome of the game.

During your interview, you will pair on adding support for a computer player to your game. You can start
 with random moves and make the AI smarter if you have time.
 0,0  0,1  0,2 
 1,0  1,1  1,2 
 2,0  2,1  2,2 
 


 
 """

#checks the board to see if anyone has won, or if there is a draw. 
def threeInARow(row1, col1, row2, col2, row3, col3, board):
  if board[row1][col1] == board[row2][col2]==board[row3][col3] !=0:
    return board[row1][col1]
  return 0
  
  
def didAnyoneWin(board):
  for i in range(0, 3):
    possibleWin = threeInARow(i,0,i,1,i,2,board)
    print(possibleWin)
    if possibleWin:
      return possibleWin
    possibleWin = threeInARow(0,i,1,i,2,i,board)
    print(possibleWin)
    if possibleWin:
      return possibleWin
  diagonal1 = threeInARow(0,0,1,1,2,2,board)
  print(diagonal1)
  if diagonal1:
    return diagonal1
  diagonal2 = threeInARow(2,0,1,1,0,2,board)
  print(diagonal2)
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

def gameloop(board, winner, turn):
    validMove = False
    while not validMove:
      try:
        row = int(input("enter the row (0 = top, 1 = mid, 2 = bottom)"))
        col = int(input("enter the col (0 = left, 1 = mid, 2 = right)"))
        validMove = validateMove(board, row, col, turn)
      except ValueError:
        print("you entered something other than an int. Don't do that!")
    print("made it out of while loop")
    board[row][col] = turn
    print(board)
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
        print("NO CONTEST!")
    return


main()
