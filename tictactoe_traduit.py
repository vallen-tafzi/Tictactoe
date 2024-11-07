# Function to display the tictactoe board in a readable format
def display_board(board):
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i + 1] + " | " + board[i + 2])
        if i < 6:
            print("--+---+--")
        else: 
            print()
            print()

# Function to check if a player has won by comparing positions against winning conditions
def player_wins(board, player):
    winning_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for condition in winning_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if there are any empty cells remaining on the board
def empty_cell(board):
    return " " in board

# Function to allow the player to make a move, with input validation for cell availability
def player_move(board, player):
    move = int(input("Enter a cell number (0-8): "))
    if board[move] == " ":
        board[move] = player
    else:
        print("Cell already taken, try again.")
        player_move(board, player)

# Function for AI to make a strategic move, checking for possible wins, blocks, and optimal positions
def ai(board, sign):
    opponent = "O" if sign == "X" else "X"
    for i in range(9):
        board_copy = board[:]
        if board_copy[i] == " ":
            board_copy[i] = sign
            if player_wins(board_copy, sign):
                return i
    for i in range(9):
        board_copy = board[:]
        if board_copy[i] == " ":
            board_copy[i] = opponent
            if player_wins(board_copy, opponent):
                return i
    corners = [0, 2, 6, 8]
    for corner in corners:
        if board[corner] == " ":
            return corner
    if board[4] == " ":
        return 4
    edges = [1, 3, 5, 7]
    for edge in edges:
        if board[edge] == " ":
            return edge
    return False

# Main function to run the game loop, managing player turns and checking for end conditions
def game():
    board = [" " for _ in range(9)]
    print("Choose game mode:")
    print("1. Play against another player")
    print("2. Play against AI")
    choice = input("Enter 1 or 2: ")
    
    current_player = "X"
    
    while empty_cell(board) and not player_wins(board, "X") and not player_wins(board, "O"):
        display_board(board)
        if current_player == "X":
            player_move(board, current_player)
            current_player = "O"
        else:
            if choice == "1":
                player_move(board, current_player)
            elif choice == "2":
                move = ai(board, current_player)
                if move is not False:
                    board[move] = current_player
            current_player = "X"
    
    display_board(board)
    if player_wins(board, "X"):
        print("X wins!")
    elif player_wins(board, "O"):
        print("O wins!")
    else:
        print("It's a tie!")

game()