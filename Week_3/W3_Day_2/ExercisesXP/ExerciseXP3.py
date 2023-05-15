# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

from ExercisesXP import Dog
import ExercisesXP
import random

print('Exercise 2')
class PetDog(Dog):
    def __init__(self,  name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained
        self.all_tricks = []
        
    def train(self):
        self.trained = True
        print(self.bark(self.name))         
    def play(self, *dogs):
        for dog in dogs:  
            self.all_tricks.append(dog)    
        all_dogs =  ', '.join(self.all_tricks) 
        sentence = f'{all_dogs} play together'
        print(sentence)
    def do_a_trick(self):
        all_tricks=[f'{self.name} does a barrel roll', f'{self.name} stands on his back legs', f'{self.name} shakes your hand', f'{self.name} plays dead']
        if self.trained:
            random_trick = random.randint(0, (len(all_tricks)-1))
            print(all_tricks[random_trick])
    

jon_dog = PetDog('Luna', 2, 10)
lily_dog = PetDog('Charlie', 3, 13)
sara_dog = PetDog('Cooper', 5, 8)
ester_dog = PetDog('Daisy', 4, 7)

jon_dog.train()
ester_dog.train()
sara_dog.train()
ester_dog.train()
lily_dog.train()
lily_dog.play(jon_dog.name, sara_dog.name, ester_dog.name)
ester_dog.do_a_trick()
sara_dog.do_a_trick()
lily_dog.do_a_trick()

print('****************')