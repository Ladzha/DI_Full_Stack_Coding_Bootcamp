from game import Game
def get_user_menu_choice():
    print('*********************\nRock, Paper, Scissors\n*********************')
    choice =input('Menu: \n (g) Play a new game \n (x) Show scores and (q)exit:')
    if choice == 'g' or choice == 'x' or choice == 'q':
        choice = choice     
    else: 
        print('You entered an irrelevant value')
    return choice
    
def print_results(results):
    # results = {'win': 0, 'loss': 0, 'draw':0} # file
    string = f'Game results:\n You won {results["win"]} times\nYou lost {results["loss"]} times\nYou drew {results["draw"]} times.\nThank you for playing!'
    return string

def main():
    while True:
        if get_user_menu_choice():
            break
        else:
            get_user_menu_choice()
    game1=Game()
    game1.play()
    

    # if input()=='q':
    #     print_results(results)
        
    