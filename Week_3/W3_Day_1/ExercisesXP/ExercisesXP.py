# # 🌟 Exercise 1: Cats
# # Instructions
# # Using this class

# # class Cat:
# #     def __init__(self, cat_name, cat_age):
# #         self.name = cat_name
# #         self.age = cat_age
# # Instantiate three Cat objects using the code provided above.
# # Outside of the class, create a function that finds the oldest cat and returns the cat.
# # Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

# print("Exercise 1")

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# my_cat = Cat('Barsik', 2)
# your_cat = Cat('Murka', 3)
# her_cat = Cat('Donny', 4)

# def oldest_cat(*cats):
#     the_oldest = cats[0].age
#     for cat in cats:       
#         if cat.age > cats[0].age:
#             the_oldest = cat
#     print(f'The oldest cat is {the_oldest.name}, and it is {the_oldest.age} years old.')

# oldest_cat(my_cat, your_cat, her_cat)

# print("****************************")


# # 🌟 Exercise 2 : Dogs
# # Instructions
# # Create a class called Dog.
# # In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# # Create a method called bark that prints the following string “<dog_name> goes woof!”.
# # Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# # Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# # Print the details of his dog (ie. name and height) and call the methods bark and jump.
# # Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# # Print the details of her dog (ie. name and height) and call the methods bark and jump.
# # Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

# print("Exercise 2")

# class Dog:
#     def __init__(self, dog_name, dog_height):
#         self.name = dog_name
#         self.height = dog_height
    
#     def bark(self):
#         print(f'{self.name} goes woof!')
        
#     def jump(self):
#         x=self.height*2
#         print(f'{self.name} jumps {x} cm high!')

# davids_dog = Dog('Rex', 50)
# print(f'David has a dog. Dog\'s name is {davids_dog.name}')
# print(f'{davids_dog.name} is {davids_dog.height} cm')
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog('Teacup', 20)
# print(f'Sara has a dog. Dog\'s name is {sarahs_dog.name}')
# print(f'{sarahs_dog.name} is {sarahs_dog.height} cm')
# sarahs_dog.bark()
# sarahs_dog.jump()

# if sarahs_dog.height > davids_dog.height:
#     bigger_dog = sarahs_dog
# else:
#     bigger_dog = davids_dog
    
# print(f'Bigger dog is {bigger_dog.name} it is {bigger_dog.height} cm')

# print("****************************")

# print("Exercise 3")
# class Song:
#     def __init__(self, lyrics: list):
#         self.lyrics = lyrics
    
#     def sing_me_a_song (self):       
#         for lyric in self.lyrics:         
#             print(lyric)
            
# stairway= Song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])
# stairway.sing_me_a_song()
# print("****************************")


# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example


print("Exercise 4")

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals  = []
    
    def add_animals (self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        
    def get_animals (self):
        for animal in self.animals:
            print(animal)
            
    def sell_animal (self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals (self):
        self.animals.sort()
        sorted_animals = {}
        for animal in self.animals:
            first_letter = animal[0]          
            if first_letter in sorted_animals.keys():
                sorted_animals[first_letter].append(animal)
            else:
                sorted_animals[first_letter] = [animal]
            self.grouped_animals ={}
            group_num = 1
        for key in sorted(sorted_animals.keys()):
            self.grouped_animals[group_num]=sorted_animals[key]
            group_num +=1

    def get_groups(self):
        self.sort_animals()
        for group_number, group_value in self.grouped_animals.items():
            print(f"{group_number} : {', '.join(group_value)}")

ramat_gan_safari = Zoo('Ramat Gan Safari')
ramat_gan_safari.add_animals('Giraffe')
ramat_gan_safari.add_animals('Bear')
ramat_gan_safari.add_animals('Lion')
ramat_gan_safari.add_animals('Baboon')
ramat_gan_safari.add_animals('Cougar')
ramat_gan_safari.add_animals('Eel')
ramat_gan_safari.add_animals('Tiger')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('Eel')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()


print("****************************")
