from game import Game

def get_user_menu_choice():
    print('*********************\nRock, Paper, Scissors\n*********************')
    user_choice = input('Menu:\n(g) Play a new game\n(x) Show scores\n(q) Exit: ').lower() 
    return user_choice

def print_results(results:dict):
    string = f'Game results:\nYou won {results["win"]} times\nYou lost {results["loss"]} times\nYou drew {results["draw"]} times.\nThank you for playing!'
    return print(string)

def main():
    results_dic = {'win': 0, 'loss': 0, 'draw': 0}
    user_choice = get_user_menu_choice()
    while user_choice != 'q':
        if user_choice == 'g':
            new_game = Game()
            result = new_game.play()      
            results_dic[result] +=1
        elif user_choice == 'x':
            print_results(results_dic)
        user_choice=get_user_menu_choice()  

main()