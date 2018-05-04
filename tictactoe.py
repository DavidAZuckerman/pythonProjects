"""Before your interview, write a program that lets two humans play a game of Tic Tac Toe in a terminal.
The program should let the players take turns to input their moves. The program should report the outcome of the game.

During your interview, you will pair on adding support for a computer player to your game. You can start
 with random moves and make the AI smarter if you have time."""

#checks the board to see if anyone has won, or if there is a draw. 
def didAnyoneWin(board):
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
    winner = 0 #If player 1 wins, winner=1. If player 2 wins, winner=2, if draw, winner=-1, if not yet finished, winner=0
    turn = 1 #turn = 1 for player 1's turn. turn=-1 for player 2's turn
    while(winner==0):
        (board, winner, turn) = gameloop(board, winner, turn)
    if winner==1:
        print("A WINNER IS PLAYER WON")
    elif winner==2:
        print("A WINNER IS PLAYER TOO")
    elif winner==-1:
        print("YOU'RE A GOOD DRAWER")
    return


main()
