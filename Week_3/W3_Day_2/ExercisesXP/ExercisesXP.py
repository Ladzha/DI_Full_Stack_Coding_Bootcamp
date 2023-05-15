# 🌟 Exercise 1 : Pets
# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.
# print('Exercise 1')
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_1 = Bengal("Barsick", 2)
chartreux_1 = Chartreux("Murka", 3)
siamese_1 = Siamese("Lola", 4)
sara_pets = Pets("Cat")
all_cats = [bengal_1, chartreux_1, siamese_1]
# print(all_cats.walk())
print('****************')

# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

print('Exercise 2')
class Dog():
    def __init__(self,  name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self, name):
        return f'{name} is barking'
    def run_speed(self):
        run_speed = self.weight/self.age*10
        return f'{self.name}\'s running speed is {self.weight} / {self.age} * 10 = {run_speed}'
        return run_speed 
    def fight(self, another_dog):
        winner_name = ''
        if self.run_speed() > another_dog.run_speed():
            # winner_name = self.name
            print(self.name)
        else: 
            winner_name = another_dog.name
            print(self.name)
        # message = 'f{winner_name} won the fight.'        
        # return message
        print(self.name)

dog_1 = Dog('Sharick', 3, 20)
dog_2 = Dog('Luky', 4, 10)
dog_3 = Dog('Lola', 6, 5)
print(dog_1.bark(dog_1.name))
print(dog_2.run_speed())
print(dog_2.fight(dog_1))
print()
print('****************')