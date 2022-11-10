import random


def player_board():
    column = 7
    while True:
        try:
            rows = int(input('How many rows (min 4, max 8): ')) # Rows selection
        except ValueError:
            print("Please input an integer from 4 to 8 inclusive")
        else:
            if rows not in range(4, 9):  # We restrict the number of rows to 4-8
                print("Please input an integer from 4 to 8 inclusive")
                continue
            else:
                break
    board = []
    for i in range(rows * column):
        board.append(0)

    return board  # Row 0 is bottom row. Column 0 is leftmost column.


def choose_computer_opponent(): # Player vs Computer or Player vs Player
    user_input = ''
    while user_input not in ["P", "C"]:
        user_input = input('Do you want to play against another player (P) or computer (C)? P or C? ')
        user_input = user_input.upper()
    if user_input == "P":
        return (False, 0)  # Human opponent

    elif user_input == "C":
        while True:
            level_list = [1, 2] # Level Selection
            try:
                user_level = int(input('Choose level of computer. 1. Easy 2. Medium: '))
            except ValueError:
                print("Please input only 1 or 2")
            else:
                if user_level not in level_list:
                    print("Please input only 1 or 2")
                    continue
                else:
                    break

        return (True, user_level)  # Computer opponent


def turn_assignment(): # Turn Selection
    while True:
        try:
            user_choice = int(input('What player do you want to be? Choose 1 or 2: '))
        except ValueError:
            print("Please input only 1 or 2")
        else:
            if user_choice not in [1, 2]:
                print("Please input only 1 or 2")
                continue
            else:
                break

    return user_choice


def turn_change(turn): # Swaps turn
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1
    else:
        turn = 1
    return turn


def player_pop(): # Pop or Insert
    user_input = ''
    while user_input not in ["Y", "N"]:
        user_input = input("Do you want to pop this disc? Y or N? ")
        user_input = user_input.upper()
        if user_input == "YES":  # Allow user to input yes instead of Y
            user_input = "Y"
        elif user_input == "NO":  # Allow user to input no instead of N
            user_input = "N"
    if user_input == "Y":
        return True
    else:
        return False


def player_col():  # defining col function for check_move ()
    while True:
        try:
            user_input = int(input("Choose which column to insert/pop 1-7: ")) - 1
        except ValueError:
            print("Choose a column from 1-7 only")
        else:
            if user_input not in range(7): # If it is not in 0-6
                print("Choose a column from 1-7 only")
                continue
            else:
                break
    return user_input


def check_move(board, turn, col, pop):
    if pop == False:  # Player decides to insert
        if board[-1 - (7 - col - 1)] == 0:  # Access board from -1, check if uppermost row slot is empty
            return True # Insert is allowed
        else:
            return False
    else:  # Player decides to pop
        if board[
            col] == turn:  # if the y[i] position of the list is disk of player (i) can choose to pop --> return True
            bool_value1 = True
        else:
            bool_value1 = False  # if y[i] position of list is disk of opposite player then cannot pop

    return bool_value1  # Return True or False depending on whether move is allowed


def apply_move(board, turn, col, pop): # Assume CheckMove returns True
    copy_of_board = board.copy()
    if pop == False:  # User inserts disc
        for i in range(int(len(board) / 7)):  # For loop to check each row of column specified
            if copy_of_board[7 * i + col] == 0:  # If slot is empty
                copy_of_board[7 * i + col] = turn  # Assign user's disc to that slot
                break  # Don't check through other rows

    else:  # User pops disc
        for i in range(int(len(board) / 7)):  # For loop to access each row of column specified
            try:
                copy_of_board[7 * i + col] = copy_of_board[7 * (i + 1) + col]  # Move entries of column down by one
            except IndexError:  # Assign 0 to top most row (since i+1 for topmost row not in range)
                copy_of_board[7 * i + col] = 0

    return copy_of_board


def check_victory(board, who_played):
    rows = int(len(board) / 7)
    # Check Vertical Victory
    check_vertical_victory1 = 0
    for r in range(rows - 3):
        for c in range(7):
            if board[7 * r + c] == 1 and board[7 * r + c + 7] == 1 and board[
                7 * r + c + 14] == 1 and board[7 * r + c + 21] == 1:
                check_vertical_victory1 = 1

    check_vertical_victory2 = 0
    for r in range(rows - 3):
        for c in range(7):
            if board[7 * r + c] == 2 and board[7 * r + c + 7] == 2 and board[
                7 * r + c + 14] == 2 and board[7 * r + c + 21] == 2:
                check_vertical_victory2 = 1

    # Check Horizontal Victory
    check_horizontal_victory1 = 0
    for r in range(rows):
        for c in range(4):
            if board[7 * r + c] == 1 and board[7 * r + c + 1] == 1 and board[
                7 * r + c + 2] == 1 and board[7 * r + c + 3] == 1:
                check_horizontal_victory1 = 1

    check_horizontal_victory2 = 0
    for r in range(rows):
        for c in range(4):
            if board[7 * r + c] == 2 and board[7 * r + c + 1] == 2 and board[
                7 * r + c + 2] == 2 and board[7 * r + c + 3] == 2:
                check_horizontal_victory2 = 1

    # Check Positive Slope
    check_positive_slope1 = 0
    for r in range(rows - 3):
        for c in range(4):
            if board[7 * r + c] == 1 and board[7 * r + c + 8] == 1 and board[7 * r + c + 16] == 1 and \
                    board[7 * r + c + 24] == 1:
                check_positive_slope1 = 1

    check_positive_slope2 = 0
    for r in range(rows - 3):
        for c in range(4):
            if board[7 * r + c] == 2 and board[7 * r + c + 8] == 2 and board[7 * r + c + 16] == 2 and \
                    board[7 * r + c + 24] == 2:
                check_positive_slope2 = 1


    # Check Negative Slope
    check_negative_slope1 = 0
    for r in range(0, rows - 3):
        for c in range(3, 7):
            if board[7 * r + c] == 1 and board[7 * r + c + 6] == 1 and board[7 * r + c + 12] == 1 and \
                    board[7 * r + c + 18] == 1:
                check_negative_slope1 = 1

    check_negative_slope2 = 0
    for r in range(0, rows - 3):
        for c in range(3, 7):
            if board[7 * r + c] == 2 and board[7 * r + c + 6] == 2 and board[7 * r + c + 12] == 2 and \
                    board[7 * r + c + 18] == 2:
                check_negative_slope2 = 1

    # checking if player 1 or player 2 win
    check_victory1 = -1 # Initialising
    check_victory2 = -1
    if check_horizontal_victory1 == 1 or check_vertical_victory1 == 1 or check_positive_slope1 == 1 or check_negative_slope1 == 1:
        check_victory1 = 1
    if check_vertical_victory2 == 1 or check_horizontal_victory2 == 1 or check_negative_slope2 == 1 or check_positive_slope2 == 1:
        check_victory2 = 1
    if check_victory1 == 1 and check_victory2 == 1: # This will check for both Players winning at the same time
        return turn_change(who_played) # Winner is the one who did not play the move
    elif check_victory1 == 1:
        return 1
    elif check_victory2 == 1:
        return 2
    else:
        return 0


def computer_move(board, turn, level):
    # Initialising Turns representing Computer and Player
    computer = turn
    player = turn_change(turn)
    # level 1
    if level == 1:
        col = random.randint(0, 6)
        pop = random.randint(0, 1)
        while check_move(board, turn, col, pop) == False:
            col = random.randint(0, 6)
            pop = random.randint(0, 1)
        return (col, pop)

    # level 2
    else:
        placeable = [0, 1, 2, 3, 4, 5, 6]  # [0,1,2,3,4,5,6] columns that computer can insert
        poppable = [0, 1, 2, 3, 4, 5, 6]  # [0,1,2,3,4,5,6] columns that computer can pop

        # Insert to win or block player winning
        for i in range(2): # Check for Computer then Player
            for c in placeable:
                if check_move(board, turn, c, False):  # If inserting is possible
                    copy_of_board = apply_move(board, turn, c, False)  # Simulate inserting for Computer
                    if check_victory(copy_of_board, turn) == turn:  # Anyone has a direct winning condition
                        return (c, False)  # Insert to block win
            turn = turn_change(turn)  # If Computer has no winning move, check for player 3-in-a-row

        # Check for columns computer should not insert which will lead to player win next move
        for c in placeable: # Iterate over the placable columns
            if check_move(board, computer, c, False):  # If inserting is possible for computer
                copy_of_board = apply_move(board, computer, c, False)  # Simulate inserting for Computer
                if check_move(copy_of_board, player, c, False):  # If inserting is possible for Player
                    copy_of_board = apply_move(copy_of_board, player, c, False) #Simulate inserting for Player
                    if check_victory(copy_of_board, player) == player:  # Player has a direct winning condition
                        placeable.remove(c)  # Remove from the columns that Computer can insert

        # Pop for computer to win; player winning
        for c in poppable: # Iterate over the poppable columns
            if check_move(board, computer, c, True):  # Check if possible to pop
                copy_of_board = apply_move(board, computer, c, True)  # Simulate popping
                if check_victory(copy_of_board, computer) == computer:
                    return (c, True) # If Computer wins, Computer should pop

                elif check_victory(copy_of_board, computer) == player:  # Player wins OR Both wins
                    if c in poppable: # To prevent removing c if not in poppable
                        poppable.remove(c)  # Remove c from poppable columns

        # Prevent pop at a column which will lead to player win next round
        # Case 1: Computer pop --> next round insert win
        for c in poppable:  # Iterate over the poppable columns
            if check_move(board, computer, c, True):  # Check if possible to pop
                copy_of_board = apply_move(board, computer, c, True)  # Simulate Computer popping
                for d in range(7):  # Player's columns
                    if check_move(copy_of_board, player, d, False):  # If possible to insert
                        copy_of_board2 = apply_move(copy_of_board, player, d, False)  # Simulate Player insert
                        if check_victory(copy_of_board2, player) == player:  # Player wins
                            if c in poppable:
                                poppable.remove(c)  # Remove c from poppable columns

        # Case 2: Pop --> next round pop win
        for c in poppable: # Iterate over the poppable columns
            if check_move(board, computer, c, True):  # Check if possible to pop
                copy_of_board = apply_move(board, computer, c, True)  # Simulate Computer popping
                for d in range(7):  # Player's columns
                    if check_move(copy_of_board, player, d, True):
                        copy_of_board2 = apply_move(copy_of_board, player, d, True)  # Simulate player pop
                        if check_victory(copy_of_board2, player) == player:
                            if c in poppable:
                                poppable.remove(c)  # Remove c from poppable columns

        # Computer's move to make
        com_move = random.randint(0, 1)  # Insert or pop

        if com_move == 0 and len(placeable) != 0:  # If insert
            col = random.randint(0, len(placeable) - 1) # Randomise remaining columns for Computer
            while check_move(board, computer, placeable[col], False) == False:
                placeable.pop(col)  # Remove that column from list
                col = random.randint(0, len(placeable) - 1)
            return (placeable[col], False)  # Insert in a placeable column

        elif com_move == 1 and len(poppable) != 0:  # If pop
            col = random.randint(0, len(poppable) - 1)  # Randomise remaining columns for Computer
            while check_move(board, computer, poppable[col], True) == False:

                poppable.pop(col)  # Remove that column from list
                if len(poppable) == 0:
                    return (placeable[random.randint(0, len(placeable) - 1)], False)  # Randomly generate column to insert if cannot pop
                col = random.randint(0, len(poppable) - 1)

            return (poppable[col], True)  # Pop in a poppable column

        else:  # Randomise everything
            col = random.randint(0, 6)
            if check_move(board, computer, col, com_move):
                return (col, com_move)


def display_board(board):
    for i in reversed(range(int(len(board) / 7))):  # Iterate no. of rows
        print(board[7 * i: 7 * i + 7])  # Slice list for each row
    print("")
    pass


def menu():
    board = player_board()  # Initialize board
    computer = choose_computer_opponent()  # Whether opponent is computer or another human
    turn = 0

    if computer[0] == True:  # Computer opponent
        player_turn = turn_assignment()  # Ask for user to choose turn
        computer_turn = turn_change(player_turn)  # Computer takes other turn
        level = computer[1]
        computer_opponent = computer[0]


    else:  # Player vs player, doesn't matter who takes which turn
        computer_opponent = False

    while True:  # Game, breaks if game ends
        turn = turn_change(turn)  # Change to next player's turn

        if turn == 1:  # Player 1 is set to human by default
            if computer_opponent == False:  # Player vs player
                col = player_col()
                pop = player_pop()

            elif computer_opponent == True and computer_turn == 1:  # Player's turn is 2
                com_move = computer_move(board, turn, level)
                col = com_move[0]
                pop = com_move[1]
                print('Computer Placed/Pop at:', col + 1)

            elif computer_opponent == True and player_turn == 1:  # Player's turn is 1
                col = player_col()
                pop = player_pop()

        else:  # Player 2's turn
            if computer_opponent == False:  # Human opponent
                col = player_col()
                pop = player_pop()

            elif computer_opponent == True and computer_turn == 2:  # Player's turn is 1
                com_move = computer_move(board, turn, level)
                col = com_move[0]
                pop = com_move[1]
                print('Computer Placed/Pop at:', col + 1)

            elif computer_opponent == True and player_turn == 2:  # Player's turn is 2
                col = player_col()
                pop = player_pop()

        if check_move(board, turn, col, pop) == True:
            board = apply_move(board, turn, col, pop)
            display_board(board)

        else:
            if pop == True:
                print("Cannot pop if bottommost disc is not yours!")
            elif pop == False:
                print("Column is filled. Choose another column")
            turn = turn_change(turn)  # If move not allowed, reset back to previous player's turn

        if check_victory(board, turn) != 0:
            print("Player", check_victory(board, turn), "has won")
            break


if __name__ == "__main__":
    menu()
