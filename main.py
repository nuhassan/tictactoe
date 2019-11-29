# --------- Global Variables -----------

# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is over yet
game_in_progress = True

# Tells us who the winner is
winner = None

# Tells us who the current player is
current_player = None


# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():

  # Ask who will start
  who_starts()

  # Show the initial game board
  display_board()

  # Loop until the game stops (winner or tie)
  while game_in_progress:

    # Handle a turn
    print(current_player + "'s turn.")
    handle_turn(current_player)

    # Check if the game is over
    is_game_over()

    # Flip to the other player
    next_turn()
  
  # Since the game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print("Congratulations " + winner + ", You Win!!.")
  elif winner == None:
    print("Tie! Good Game!!")
  rematch = input("Rematch?(Y or N): ")
  while rematch not in ["y", "Y", "n", "N"]:
    rematch = input("Rematch?(Y or N): ")
  if rematch.upper() == "Y":
    reset_board()
    play_game()


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     7 | 8 | 9")
  print("---------     ---------")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print("---------     ---------")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     1 | 2 | 3")
  print("\n")

# Choose who starts the game
def who_starts():

  global current_player
  starting_player = input("Who will start the game, X or O?: ")

  if(starting_player != "X" and starting_player != "O" and starting_player != "x" and starting_player != "o"):
    print("Invalid Respose. Try again.")
    who_starts()
  else : current_player = starting_player.upper()

# Handle a turn for an arbitrary player
def handle_turn(player):

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:
    # Get position from player
    position = input("Choose an empty spot from 1-9: ")

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose an empty spot from 1-9: ")

    # Put the game piece on the board
    if(position == "1" or position == "2" or position == "3"):
       # Also make sure the spot is available on the board
      if board[int(position) + 5] == "-":
        valid = True
        board[int(position) + 5] = player
      else:
        print(position + " is not empty. Try Again.")
      
    elif(position == "7" or position == "8" or position == "9"):
   
      if board[int(position) - 7] == "-":
        valid = True
        board[int(position) - 7] = player
        
      else:
        print(position + " is not empty. Try Again.")

    else :
      if board[int(position) - 1] == "-":
        valid = True
        board[int(position) - 1] = player
      else:
        print(position + " is not empty. Try Again.")

  # Show the game board
  display_board()


# Check if the game is over
def is_game_over():
  has_winner()
  is_tied()


# Check to see if somebody has won
def has_winner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
  winning_row = check_rows()
  winning_col = check_columns()
  winning_diag = check_diagonals()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif winning_col:
    winner = winning_col
  elif winning_diag:
    winner = winning_diag
  else:
    winner = None


# Check the rows for a win
def check_rows():
  # Set global variables
  global game_in_progress
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_in_progress = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or return None if there was no winner
  else:
    return None


# Check the columns for a win
def check_columns():
  # Set global variables
  global game_in_progress
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_in_progress = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_in_progress
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_in_progress = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Or return None if there was no winner
  else:
    return None


# Check if there is a tie
def is_tied():
  # Set global variables
  global game_in_progress
  # If board is full
  if "-" not in board:
    game_in_progress = False
    return True
  # Else there is no tie
  else:
    return False


# Flip the current player from X to O, or O to X
def next_turn():
  # Global variables we need
  global current_player
  # If the current player was X, make it O
  if current_player == "X":
    current_player = "O"
  # Or if the current player was O, make it X
  elif current_player == "O":
    current_player = "X"

# Reset playing board and all global variables
def reset_board():
  
  global current_player
  global game_in_progress
  global winner
  global board

  current_player = None
  game_in_progress = True
  winner = None

  for x in range(9):
    board[x] = "-"
  
# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()