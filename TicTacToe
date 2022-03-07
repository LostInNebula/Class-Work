import random

def print_board(board):
    print(board[0],board[1], board[2])
    print(board[3],board[4], board[5])
    print(board[6],board[7], board[8])

def open_spots(board):
    emptyspace = list()
    for i in range(len(board)):
        if board[i] == "-":
            emptyspace.append(i)
    return emptyspace

def random_move(board, symbol):
    random.choice(open_spots(board))
    board[random.choice(open_spots(board))] = symbol
    print_board(board)

def check_three(board, idx1, idx2, idx3):
    if board[idx1] == "X" and board[idx2] == "X" and board[idx3] == "X":
        return "X"
    if board[idx1] == "O" and board[idx2] == "O" and board[idx3] == "O":
        return "O"
    else: '-'

def winner(board):

    combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for i in combos:
        if check_three(board, i[0], i[1], i[2]) == "X":
            return "X"
        if check_three(board, i[0], i[1], i[2]) == "O":
            return "O"

    open_spots(board)
    if check_three(board, i[0], i[1], i[2]) != "X" and check_three(board, i[0], i[1], i[2]) != "O":
        if open_spots(board) == []:
            return "D"
        else:
            return "-"

def tic_tac_toe():
    board = ["-","-","-","-","-","-","-","-","-",]

    random_move(board, "O")
    random_move(board, "X")
    while winner(board) == "-" and winner(board) != "X" and winner(board) != "O" and open_spots(board) != []:
        random_move(board, "O")
        print(board)
        if winner(board) != "O" and open_spots(board) != []:
            random_move(board, "X")
            print(board)
    return winner(board)

if __name__ == '__main__':
    tic_tac_toe()
