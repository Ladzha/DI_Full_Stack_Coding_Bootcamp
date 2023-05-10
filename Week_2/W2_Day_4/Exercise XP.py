print("Exercise 1")
def display_message(lesson):
    print(f"I am learning {lesson} in this course ")
display_message("Python")
print("*****************")

print("Exercise 2")
def favorite_book(title):   
    print(f"One of my favorite books is {title}.")
favorite_book('Alice in Wonderland')
print("*****************")

print("Exercise 3")
def describe_city(city, country='Holland'):   
    print(f"{city} is in {country}.")
describe_city('London', 'England')
print("*****************")


print("Exercise 4")
import random

def compare_numbers(num1, num2):   
    random_number1 = random.randint(num1, num2)
    random_number2 = random.randint(1, 100)
    
    if random_number1 == random_number2:
        print("Mathing numbers")
    else:
        print(f"{random_number1} and {random_number2} two different numbers")


compare_numbers(1,100)

print("*****************")


print("Exercise 5")
def make_shirt(size='L', text='I love Python'):   
    
    print(f"The size of the shirt is {size} and the text is {text}")
    
make_shirt('L')
make_shirt('M')
make_shirt('S', 'I love Israel')

#Bonus
def make_shirt(**kwargs):   
    
    print(f"The size of the shirt is {kwargs} and the text is {kwargs}")    
    
make_shirt(size='S', text='I love Israel')
print("*****************")

print("Exercise 6")
def show_magicians(magician_names):
    for name in magician_names:
        print(name)

show_magicians(['Harry Houdini', 'David Blaine', 'Criss Angel'])

def make_great(magician_names):
    for name in magician_names:
        name += " the Great" 
        print(name)

make_great(['Harry Houdini', 'David Blaine', 'Criss Angel'])
show_magicians(['Harry Houdini', 'David Blaine', 'Criss Angel'])
print("*****************")

print("Exercise 7")
import random

def get_random_temp(season):
    if season == 'winter':
        print('Winter')
        return(random.randint(-10, 16))  
    elif season == 'spring':
        print('Spring')
        return(random.randint(1, 20))
    elif season == 'summer':
        print('Summer')
        return(random.randint(17, 40))
    elif season == 'autumn':
        print('Autumn')
        return(random.randint(-1, 32))
def main(season):
    season = input('Type a season: ')
        
    temperature = get_random_temp(season)
    print(f'The temperature right now is {temperature} degrees Celsius.')
    if temperature < 0:
        print('Brrr, that\'s freezing! Wear some extra layers today')
    elif 0 > temperature < 16:
        print('Quite chilly! Don\'t forget your coat')
    elif 16 > temperature < 23:
        print('Good weather')
    elif 24 > temperature < 32:
        print('Quite hot! Don\'t forget to drink water')
    else:
        print('It\'s super hot!')
main(1)

print("*****************")