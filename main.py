import random


def display_board(board):
    # Imprime o tabuleiro
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        for col in range(3):
            print(f"|   {board[row * 3 + col]}   ", end="")
        print("|\n|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    while True:
        move = int(input("Digite seu movimento: "))
        if move < 1 or move > 9:
            print("Movimento inválido. Tente novamente.")
        elif board[move - 1] != " ":
            print("Campo ocupado. Tente novamente.")
        else:
            board[move - 1] = "O"
            break


def make_list_of_free_fields(board):
    free_fields = []
    for i in range(len(board)):
        if board[i] == " ":
            free_fields.append(i + 1)
    return free_fields


def victory_for(board, sign):
    # Verifica se há vitória nas linhas
    for row in range(0, 9, 3):
        if all(board[row + col] == sign for col in range(3)):
            return True

    # Verifica se há vitória nas colunas
    for col in range(3):
        if all(board[col + 3 * row] == sign for row in range(3)):
            return True

    # Verifica se há vitória na diagonal principal
    if all(board[i] == sign for i in range(0, 9, 4)):
        return True

    # Verifica se há vitória na diagonal secundária
    if all(board[i] == sign for i in range(2, 7, 2)):
        return True

    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    move = random.choice(free_fields)
    board[move - 1] = "X"


def play_game():
    board = [" "] * 9
    board[4] = "X"  # Primeiro movimento do computador

    display_board(board)

    while True:
        enter_move(board)
        display_board(board)

        if victory_for(board, "O"):
            print("Você ganhou!")
            break

        if len(make_list_of_free_fields(board)) == 0:
            print("Empate!")
            break

        draw_move(board)
        display_board(board)

        if victory_for(board, "X"):
            print("O computador ganhou!")
            break


play_game()
