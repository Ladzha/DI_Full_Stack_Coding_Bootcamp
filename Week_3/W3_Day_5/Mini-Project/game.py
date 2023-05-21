import random
class Game():
    def __init__(self):
        self.user_item = self.get_user_item()
        self.computer_item = self.get_computer_item()
        
    def get_user_item(self):  
        user_item = input('Select (r)rock, (p)paper, (s)scissors:  ').lower()
        choices = ['r', 'p', 's']
        while user_item not in choices:
            user_item = input('Select (r)rock, (p)paper, (s)scissors:  ').lower()
        return user_item
    
    def get_computer_item(self):
        choices = ['r', 'p', 's']
        computer_item = random.choice(choices)
        return computer_item
    
    def get_game_result(self):
        if self.user_item==self.computer_item:
            return 'draw'
        elif self.user_item == 'p' and self.computer_item == 'r' or self.user_item == 'r' and self.computer_item == 's' or self.user_item == 's' and self.computer_item == 'p':
            return 'win'
        elif self.computer_item == 'p' and self.user_item == 'r' or self.computer_item == 'r' and self.user_item == 's' or self.computer_item == 's' and self.user_item == 'p':
            return 'loss'
    
    def play(self):
        result = self.get_game_result() 
        print(f'You selected: {self.user_item}. The computer selected: {self.computer_item}. You {result}')
        return result
    