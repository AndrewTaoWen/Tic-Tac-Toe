from random import randrange


def clear_screen():
    from os import system, name

    if name == 'nt':
        system('cls')
    else:
        system('clear')


def print_board(board):
    for row in board:
        print(*row)
    print()


def check_win(board, user_char, comp_char):
    '''
    return 1 if player wins
    return 2 if computer wins
    return 0 if no one wins
    '''
    win = 0
    # mapping the characters to result value
    winner = {}
    winner[player_char] = 1
    winner[comp_char] = 2

    if board[0][0] == board[1][1] == board[2][2] != '#':
        win = winner[board[0][0]]
    elif board[2][0] == board[1][1] == board[0][2] != '#':
        win = winner[board[2][0]]
    else:
        for i in range(3):
            if board[i][0] != '#' and board[i].count(board[i][0]) == 3:
                win = winner[board[i][0]]
                break
            if board[0][i] == board[1][i] == board[2][i] != '#':
                win = winner[board[0][i]]
                break

    return win


def computer_move(board, comp_char):
    comp_move_row = randrange(3)
    comp_move_col = randrange(3)

    while board[comp_move_row][comp_move_col] != '#':
        comp_move_row = randrange(3)
        comp_move_col = randrange(3)
    print('Computer Move')
    board[comp_move_row][comp_move_col] = comp_char


def player_move(board, player_char):
    user_input = input('Choose your row and column(1 to 3) seperated by comma(X,Y): ')

    while ',' not in user_input:
        print('invalid input, please try again')
        user_input = input('Choose your row and column(1 to 3) seperated by comma(X,Y): ')

    player_move_row, player_move_col = map(int, user_input.split(','))

    while board[player_move_row - 1][player_move_col - 1] != '#':
        print('Spot is taken, try again.\n')
        player_move_row, player_move_col = map(int, input(
            'Choose your row and column(1 to 3) seperated by comma(X,Y): ').split(','))
    board[player_move_row - 1][player_move_col - 1] = player_char


play = True

while play:

    player_char = input('Choose a character(0/X): ')
    comp_char = 'X' if player_char == '0' else '0'
    play_count = 1
    board = [
        ['#', '#', '#'],
        ['#', '#', '#'],
        ['#', '#', '#']
    ]

    print_board(board)

    while play_count <= 9:

        result = check_win(board, player_char, comp_char)
        if result == 1:
            print('Player has won!')
            break
        elif result == 2:
            print('Computer has won!')
            break

        if play_count % 2 != 0:
            player_move(board, player_char)
            play_count += 1

        else:
            computer_move(board, comp_char)
            play_count += 1

        print_board(board)
    else:
        print('Tie game!')

    play_again = input('Play again?(Y/N): ')

    if play_again == 'N':
        print('Thank you for playing.')
        play = False
    else:
        clear_screen()