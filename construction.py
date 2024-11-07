def display_board(board):
    for i in range(0, 9, 3):
        print(board[1] + " | " + board[i + 1] + " | " + board[i +2])
        if i < 6:
            print("--+---+--")

            