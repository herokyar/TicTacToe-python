#Tic-Tac-Toe
#Plays the game of tic-tac-toe against a human opponent

#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#display instructions
def display_instruct():
    """Display game instructions."""
    print(
    """
    Welcome to the greatest intellectual challange of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.

    You will make your move known by entering a number, 0-8. The number
    will correspond to the board position as illustrated:

            
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Prepare yourself, human. The ultimate battle is about to begin. \n
    """
    )
    
#ask yes no function
def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response


#move = ask_number("where will you move? (0-8):", 0, NUM_SQUARES)

#ask number function
def ask_number(question, low, high, step):
    """ask for a number within a range."""
    response = None
    while response not in range (low, high, step):
        response = int(input(question))
    return response

#pieces function
def pieces():
    """determine if player or computer goes first."""
    go_first = ask_yes_no("do you reqire the first move? (y/n): ")
    if go_first == "y":
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        computer = X
        human = O
    return computer, human


#new board function
def new_board():
    """create new game board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

#display board function
def display_board(board):
    """display game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])    
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


#legal moves function
def legal_moves(board):
    """create list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

#winner function
def winner(board):
    """determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

#human move function
def human_move(board, human):
    """get human move."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        step = int(input("enter step size:"))   #added later
        move = ask_number("where will you move? (0-8):", 0, NUM_SQUARES, step)
        if move not in legal:
            print("\nthat square is already occupied, foolish human.choose another\n")
    print("Fine...")
    return move


#computer move function
def computer_move(board, computer, human):
    """make computer move."""
    #make a copy to work with since function will be changing list
    board = board[:]

    
    #the best positions to have , in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I shall take square number", end=" ")

    #if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #done checking this move, undo it
        board[move] = EMPTY


    #if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        #done checking this move, undo it
        board[move] = EMPTY

    #since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

#next turn function
def next_turn(turn):
    """switch turns."""
    if turn == X:
        return 0
    else:
        return X

#congrat winner function
def congrat_winner(the_winner, computer, human):
    """congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It is a tie!\n")

    if the_winner == computer:
        print("as I predicted, human, I am triumphant once more.   \n" \
              "Proof that computers are superior to humans in all regards.")

    elif the_winner == human:
        print("No, no! It cannot be! Somehow you tricked me, human, \n" \
                "But never again!, I, the computer, so swear it!")

    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me. \n" \
              "Celebrate today..  for this is the best you will ever achieve.")

#main function
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

#start the program
main()
input("\n\npress the enter key to quit.")
































              
    













