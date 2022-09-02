def display_board(board):
    print('\n' * 100)
    print(board[7] +'|'+ board[8] + '|' + board[9])
    print(board[4] +'|'+ board[5] + '|' + board[6])
    print(board[1] +'|'+ board[2] + '|' + board[3])
    pass
def player_input():
    maker = ''
    while maker != 'X' and maker != 'O':
        maker = input("Player 1 chose X or O: ")
    player1 = maker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)
    pass
def place_marker(board, marker, position):
    board[position] = marker
    return board
    pass
def win_check(board, mark):
    for i in range(1,4):
        if board[i] == board[i+3] == board[i+6]:
            if mark == board[i]:
                return True
    for i in range(1,8,3):
        if board[i] == board[i+1] == board[i+2]:
            if mark == board[i]:
                return True
    if board[1] == board[5] == board[9]:
        if board[1] == mark:
            return True
    if board[3] == board[5] == board[7]:
        if board[3] == mark:
             return True
    return False
    pass
def space_check(board, position):
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i) :
            return False
    return True
    pass
def player_choice(board):
    choice = 1000
    while choice not in range(1,10):
        choice = int(input('Choose your next position'))
        if choice not in range(1,10):
            print('Please choose your number from 1 to 9')
        if space_check(board, choice) == False:
            print('Your choice is not free pls choose again')
            choice = 1000
    return int(choice)
    pass
def replay():
    ans = input("Do you want play again pls type Y/N")
    while ans not in ['Y','N']:
        ans = input("Pls type Y or N")
    if ans == 'Y':
        return True
    else:
        return False
    pass


print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here
    game_on = True
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    # pass
    while game_on:
        print('\n' * 100)
        display_board(board)
        (player1, player2) = player_input()
        gamefinish = True
        while gamefinish:
        # Player 1 Turn
             position = player_choice(board)
             place_marker(board, player1, position)
             print('\n' * 100)
             display_board(board)
             if win_check(board, player1):
                 print("Congratulate player1")
                 gamefinish = False
                 continue
             else:
                if full_board_check(board):
                 print("Draw game")
                 gamefinish = False
                 continue
        # Player2's turn.
             position = player_choice(board)
             place_marker(board, player2, position)
             print('\n' * 100)
             display_board(board)

        # pass

             if win_check(board, player2):
                 print("Congratulate player2")
                 gamefinish = False
             else:
                if full_board_check(board):
                 print("Draw game")
                 gamefinish = False
        # replay
        if replay():
            game_on = True
            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        else:
            game_on = False

    break