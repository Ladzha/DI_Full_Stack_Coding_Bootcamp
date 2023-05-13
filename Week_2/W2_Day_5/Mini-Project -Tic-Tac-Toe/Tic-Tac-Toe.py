
board = [["  ", "  ", "  "], 
        ["  ", "  ", "  "], 
        ["  ", "  ", "  "]]
row = -1
column = -1
print("Welcome to Tic Tac Toe")
decor_line = '*'*17  
line = "* ---|----|---- *"
line_end = "*    |    |     *"

def display_board(board): 
  row = lambda row_num : f'* {board[row_num][0]} | {board[row_num][1]} | {board[row_num][2]}  *'
  print("Tic Tac Toe")
  print(decor_line)
  print(row(0))
  print(line)
  print(row(1))
  print(line)
  print(row(2))
  print(line)
  print(line_end)
  print(decor_line)
display_board(board)

symbol = ('x ','o ')
def player_input():
  turn = 1
  current_symbol = symbol[0] if turn %2 ==0 else symbol[1]
  print(f'Player "{current_symbol}" your turn')    
  row = int(input("Enter row from 1 to 3: "))
  while row > 3 or row < 1:
    row = int(input("Enter row from 1 to 3: "))   
  column = int(input("Enter column from 1 to 3: "))
  while column > 3 or column < 1:
    column = int(input("Enter column from 1 to 3: "))
  if board[row-1][column-1] == "  ":
    board[row-1][column-1] = current_symbol
    turn+=1
    print(board[row-1][column-1])   
  else:
    ('Try again')
player_input()
display_board(board)
player_input()
display_board(board)





# board[player_1_move_1-1][player_1_move_2-1] = "x"
# print(board[player_1_move_1-1][player_1_move_2-1])

