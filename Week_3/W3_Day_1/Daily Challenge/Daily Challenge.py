# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output:
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# Test your code and make sure you get the same results as the example above.
# Bonus: nicely line the text in columns as seen in the example above. Use string formatting.


# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].

# Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to get a list of the animals.

class Farm():
    def __init__(self, farmname):
        self.farmname = farmname
        self.farm_animals_dict  = {}
    
    def add_animal (self, farm_animal, animal_number = 1):
        if farm_animal not in self.farm_animals_dict.keys():
            self.farm_animals_dict[farm_animal] = animal_number
        else:
            self.farm_animals_dict[farm_animal] += animal_number 
    def get_info(self):
             
        text = f'{self.farmname} farm'
        for farm_animal, animal_number in self.farm_animals_dict.items():
            text += f'\n {farm_animal} : {animal_number}' 
        text +='\n \t E-I-E-I-0!'
        return text
    def  get_animal_types(self):
        sorted_list=[]
        for name in self.farm_animals_dict.keys():
            sorted_list.append(name)
        sorted_list.sort()
        return sorted_list
    def get_short_info(self):
        result = f'McDonald\'s farm has '
        for name in self.farm_animals_dict.keys():         
            result += name + ', '
        return result  
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())