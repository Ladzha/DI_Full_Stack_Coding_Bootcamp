# import game
def get_user_menu_choice():
    print('*********************\nRock, Paper, Scissors\n*********************')
    print('Menu: \n (g) Play a new game \n (x) Show scores and exit')
    
def user_move():
    user_input = input('Select (r)rock, (p)paper, (sscissors:  ')
    return user_input
    
def show_result():
    string = f'You chose: {user_move}. The computer chose: {game.random_choice}. Result: {game.result}'
    return string

show_menu()