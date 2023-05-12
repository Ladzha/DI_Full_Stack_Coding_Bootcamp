
board = [["1/1", "1/2", "1/3"], 
        ["2/1", "2/2", "2/3"], 
        ["3/1", "3/2", "3/3"]]
row = 1
column = 1
def display_board(board):
    print("Welcome to Tic Tac Toe")
    print("Tic Tac Toe")
    print("*********************")
    for i in range(3):
        print(f'* {board[0][0]}  | {board[0][0]}  |  {board[0][0]} *')
        print(f'* -----|------|----- *')
        print("*********************")
display_board(board)


# def player_input(player):
#     row = int(input("Enter row: "))
#     if row > 3 or row < 1:
#         while row > 3 or row < 1:
#             row = int(input("Enter row: "))   
#     column = int(input("Enter column: "))
#     if column > 3 or row < 1:
#         while column > 3 or column < 1:
#             column = int(input("Enter column: "))
#     return row, column     
# player_input("player_X")


player_1_move_1 = int(input("Enter row: "))
player_1_move_2 = int(input("Enter column: "))

board[player_1_move_1-1][player_1_move_2-1] = "x"
print(board[player_1_move_1-1][player_1_move_2-1])

# def display_board(board):
#     print("Welcome to Tic Tac Toe")
#     print("Tic Tac Toe")
#     print("*********************")
    
#     print(f'*  {board[0][0]}   |  {board[0][0]}   |   {board[0][0]}   *')
#     print(f'* -----|-----|----- *')
#     print(f'* {board[0][0]}  | {board[0][0]}    |  {board[0][0]}    *')
#     print(f'* -----|-----|----- *')
#     print(f'*    {board[0][0]}  |   {board[0][0]}  |  {board[0][0]}    *')
#     print("*********************")
# display_board(board)

# if row == 1:
# for row in range(3):
#         for column in board[0]:
#             if column == 2:
#                 print("lolololololol")
#         # print(row)
# if row == 2:
#     for row in board[1]:
#         print(row)
# if row == 3:
#     for row in board[2]:
#         print(row)