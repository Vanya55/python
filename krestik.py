import random

doska = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
kombin = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner(board, player):
    for combo in kombin:
        if all(board[pos//3][pos%3] == player for pos in combo):
            return True
    return False

def is_board_full(board):
    return all(cell != "-" for row in board for cell in row)

def player_move(player):
    while True:
        row = int(input("Введите номер строки (0, 1 или 2): "))
        col = int(input("Введите номер столбца (0, 1 или 2): "))
        if 0 <= row < 3 and 0 <= col < 3 and doska[row][col] == "-":
            doska[row][col] = player
            break
        else:
            print("Недопустимый ход. Попробуйте снова.")

print("Выберите режим игры:")
print("1. Игра с компьютером")
print("2. Игра с вторым игроком")

mode = input()

if mode == "1":
    while True:
        print_board(doska)
        player_move("X")

        if check_winner(doska, "X"):
            print_board(doska)
            print("Игрок X победил!")
            break
        elif is_board_full(doska):
            print_board(doska)
            print("Ничья!")
            break

        comp_move = random.choice([pos for pos in range(9) if doska[pos//3][pos%3] == "-"])
        doska[comp_move//3][comp_move%3] = "O"

        if check_winner(doska, "O"):
            print_board(doska)
            print("Компьютер победил!")
            break
        elif is_board_full(doska):
            print_board(doska)
            print("Ничья!")
            break

elif mode == "2":
    while True:
        print_board(doska)
        player_move("X")

        if check_winner(doska, "X"):
            print_board(doska)
            print("Игрок X победил!")
            break
        elif is_board_full(doska):
            print_board(doska)
            print("Ничья!")
            break

        print_board(doska)
        player_move("O")

        if check_winner(doska, "O"):
            print_board(doska)
            print("Игрок O победил!")
            break
        elif is_board_full(doska):
            print_board(doska)
            print("Ничья!")
            break

else:
    print("Недопустимый режим. Выберите 1 или 2.")
