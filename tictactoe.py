"""Before your interview, write a program that lets two humans play a game of Tic Tac Toe in a terminal.
The program should let the players take turns to input their moves. The program should report the outcome of the game.

During your interview, you will pair on adding support for a computer player to your game. You can start
 with random moves and make the AI smarter if you have time."""

def gameloop(board, winner, turn):
    #player = ""
    #if turn == 1:
    #    player="X"
    #else:
    #    player="O"
    row = input("enter the row (0 = top, 1 = mid, 2 = bottom)")
    col = input("enter the col (0 = left, 1 = mid, 2 = right)")
    

    return (board, -1, (turn*-1))


def main():
    board = [[0,0,0],[0,0,0],[0,0,0]]
    winner = 0 #If player 1 wins, winner=1. If player 2 wins, winner=2, if draw, winner=-1, if not yet finished, winner=0
    turn = 1 #turn = 1 for player 1's turn. turn=-1 for player 2's turn
    while(winner==0):
        (board, winner) = gameloop(board, winner, turn)
    if winner==1:
        print("A WINNER IS PLAYER WON")
    elif winner==2:
        print("A WINNER IS PLAYER TOO")
    elif winner==-1:
        print("YOU'RE A GOOD DRAWER")
    return


main()
