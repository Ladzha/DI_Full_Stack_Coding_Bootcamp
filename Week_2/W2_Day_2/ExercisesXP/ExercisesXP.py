'''
🌟 Exercise 1 : Set
Create a SET called my_fav_numbers with all your favorites numbers.
Add two new numbers to the set.
Remove the last number.
Create a set called friend_fav_numbers with your friend's favorites numbers.
Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
'''
print("Exercise 1")
my_fav_numbers = {1, 2, 3, 4, 5, 6}
print('my favorites numbers: ', my_fav_numbers)
my_fav_numbers.update([0,7])
print('my favorites numbers + adding numbers: ' , my_fav_numbers)
my_fav_numbers.pop()
print('my favorites numbers - last: ' , my_fav_numbers)
friend_fav_numbers = {7, 8, 9, 10, 11, 12}
print('my friend favorites numbers: ' , friend_fav_numbers)
our_fav_numbers=my_fav_numbers
our_fav_numbers.update(friend_fav_numbers)
print('our favorites numbers: ' , our_fav_numbers)

print("****************************")

'''
🌟 Exercise 2 :  Tuple
Given a tuple which value is integers, is it possible to add more integers to the tuple?

No. Tuples are immutable. You cannot change them. 
'''

'''
🌟 Exercise 3: List
Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

Remove “Banana” from the list.
Remove “Blueberries” from the list.
Add “Kiwi” to the end of the list.
Add “Apples” to the beginning of the list.
Count how many apples are in the basket.
Empty the basket.
Print(basket)

'''
print("Exercise 3")

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print("Basket list", basket)
basket.remove("Banana")
basket.pop()
print("Basket List - banana and Blueberries", basket)
basket.append("Kiwi")
basket.insert(0, "Apples")
print("Basket List + kiwi and apples", basket)
apples_number=basket.count("Apples")
print(f"There are {apples_number} apples in the basket")
basket.clear()
print("Empty basket", basket)
print("****************************")

'''
🌟 Exercise 4: Floats
Recap - What is a float? What is the difference between an integer and a float?
Can you think of another way to generate a sequence of floats?
Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don't hard-code the sequence).
'''
print("Exercise 4")

list_conteiner = []
for i in range(1, 6):
    list_conteiner.append(i + 0.5)
    list_conteiner.append(i+1)
list_conteiner.pop()   
print(list_conteiner)

print("****************************")

'''
🌟 Exercise 5: For Loop
Use a for loop to print all numbers from 1 to 20, inclusive.
Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

'''
print("Exercise 5")

for i in range(1,21):
    print(i)

print("******")

for i in range(1,21):
    if i%2 == 0:
        print(i)

print("****************************")

'''
🌟 Exercise 6 : While Loop
Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

'''
print("Exercise 6")

user_name = ''
while user_name != "Alla":
    user_name = input("What is your name? ")    
print("Thats my name too!")
print("****************************")

'''

🌟 Exercise 7: Favorite Fruits
Ask the user to input their favorite fruit(s) (one or several fruits).
Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
Store the favorite fruit(s) in a list (convert the string of words into a list of words).
Now that we have a list of fruits, ask the user to input a name of any fruit.

If the user's input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
If the user's input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
'''
print("Exercise 7")

fruits = input("What is your favorite fruits? Separate the fruits with a single space ")
fruits_list = fruits.split(" ")
new_fruit = input("Input a name of any fruit ")

if new_fruit in fruits_list:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')    
    
print("****************************")


'''
Exercise 8: Who Ordered A Pizza ?
Write a loop that asks a user to enter a series of pizza toppings, when the user inputs 'quit' stop asking for toppings.
As they enter each topping, print a message saying you'll add that topping to their pizza.
Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
'''
print("Exercise 8")
price = 10
user_topping = ''
toppings = []
while user_topping != "quit":
    user_topping = input('Enter a series of pizza toppings: ')
    if user_topping != "quit":
        print(f'We will add {user_topping} topping to your pizza')
        toppings.append(user_topping)
        price += 2.5
print(f'Your pizza will cost {price}')
print("****************************")

'''
Exercise 9: Cinemax
A movie theater charges different ticket prices depending on a person's age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Ask a family the age of each person who wants a ticket.

Store the total cost of all the family's tickets and print it out.

A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
At the end, print the final list.
'''
print("Exercise 9")

user_input = input('Put the age of each person who wants a ticket. Separate the ages with a single space ')

persons_list= user_input.split(" ")
total_price = 0
for i in range(len(persons_list)):
    persons_list[i] = int(persons_list[i])    
    if persons_list[i] <=3:
        ticket_price = 0
    elif 3 < persons_list[i] <= 12:
        ticket_price  = 10
    else:
        ticket_price  = 15
    total_price += ticket_price
print(total_price)

teen_names = ["John", "Emma", "Sam", "Alex", "Samantha", "Sara"]

for i in teen_names:
    age = int(input(f'Put your age {i}: '))
    if 16 < age < 21:
        teen_names.remove(i)   
        
print(teen_names)

print("****************************")

'''
Exercise 10 : Sandwich Orders.
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

Use the above list called sandwich_orders.
Make an empty list called finished_sandwiches.
As each sandwich is made, move it to the list of finished sandwiches.
After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.
'''
print("Exercise 10")

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

finished_sandwiches = []

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f'I made your {sandwich}')
    
print("****************************")

'''
Exercise 11 : Sandwich Orders#2
Using the list sandwich_orders from the previous exercise, make sure the sandwich 'pastrami' appears in the list at least three times.
Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
Make sure no pastrami sandwiches end up in finished_sandwiches.

'''
print("Exercise 11")

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
sandwich_orders.extend(["Pastrami sandwich","Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich"])

print("The deli has run out of pastrami")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f'I made your {sandwich}')