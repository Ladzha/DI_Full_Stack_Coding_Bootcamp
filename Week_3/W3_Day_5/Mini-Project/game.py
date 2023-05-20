
import random
class Game():
    def __init__(self) -> None:
        pass
    
    def get_user_item(self):
        while True:
            user_item = input('Select (r)rock, (p)paper, (s)scissors:  ')
            if(user_item=='r' or user_item=='p' or user_item=='s'):
                break
            else:
                print('You entered an irrelevant value')
        return user_item
    
    def get_computer_item(self):
        choices = ['r', 'p', 's']
        computer_item = random.choice(choices)
        return computer_item
    
    def get_game_result(self):
        results = {'win': 0, 'loss': 0, 'draw':0}
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        if user_item==computer_item:
            results["draw"]+=1
            result = 'draw' 
            # print('Draw')
        elif user_item > computer_item:
            results["won"]+=1
            # print('User won')
        elif computer_item>user_item:
            results["loss"]+=1
            result = 'lost'
            # print('Computer won')
        return result
    
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result() 
        print(f'You selected: {user_item}. The computer selected: {computer_item}. You {result}')
        return result
    


game1=Game()
game1.play()

    


        # result=''
        # print(f'My move - {random_choice}') 
    # print('Let\'s play a game')

    # player_won=0
    # player_lost=0
    # player_drew=0

    # print(f'Game results:\n You won {player_won} times\nYou lost {player_lost} times\nYou drew {player_drew} times')
    # print('Thank you for playing!')


