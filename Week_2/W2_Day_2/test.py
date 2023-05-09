# # # print("Exercise 1")
# # # my_fav_numbers = {1, 2, 3, 4, 5, 6}
# # # print('my favorites numbers: ', my_fav_numbers)
# # # my_fav_numbers.append(7)
# # # my_fav_numbers.insert(0, 8)
# # # print('my favorites numbers + adding numbers: ' , my_fav_numbers)
# # # my_fav_numbers.pop()
# # # print('my favorites numbers - last: ' , my_fav_numbers)
# # # friend_fav_numbers = {7, 8, 9, 10, 11, 12}
# # # print('my friend favorites numbers: ' , friend_fav_numbers)
# # # our_fav_numbers=my_fav_numbers+friend_fav_numbers
# # # print('our favorites numbers: ' , our_fav_numbers)

# # # print("****************************")

# # print("Exercise 3")

# # basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# # print("Basket list", basket)
# # basket.remove("Banana")
# # basket.remove("Blueberries")
# # print("Basket List - banana and Blueberries", basket)
# # basket.append("Kiwi")
# # basket.insert(0, "Apples")
# # print("Basket List + kiwi and apples", basket)
# # apples_number=basket.count("Apples")
# # print(f"There are {apples_number} apples in the basket")
# # basket.clear()
# # print("Empty basket", basket)
# # print("****************************")


# # print("Exercise 7")




# # print("Exercise 9")

# # family_members_age = input('Put the age of each person who wants a ticket. Separate the ages with a single space')

# # persons_list=family_members_age.split(" ")
# # print(family_members_age)

# # if age <=3:
# #     price = 0
# # elif 3 < age <= 12:
# #     price = 10
# # else:
# #     price = 15




# # print("Exercise 10")

# # sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

# # finished_sandwiches = []

# # for sandwich in sandwich_orders:
# #     finished_sandwiches.append(sandwich)
# #     print(f'I made your {sandwich}')

# # print("Exercise 11")

# # sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# # sandwich_orders.extend(["Pastrami sandwich","Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich"])

# # print("The deli has run out of pastrami")
# # while "Pastrami sandwich" in sandwich_orders:
# #     sandwich_orders.remove("Pastrami sandwich")
    
# # for sandwich in sandwich_orders:
# #     finished_sandwiches.append(sandwich)
# #     print(f'I made your {sandwich}')

# # list_conteiner = []
# # for i in range(1, 6):
# #     list_conteiner.append(i + 0.5)
# #     list_conteiner.append(i+1)

# # list_conteiner.pop()   
# # print(list_conteiner)

# print("Exercise 8")
# price = 10
# user_topping = ''
# toppings = []
# while user_topping != "quit":
#     user_topping = input('Enter a series of pizza toppings: ')
#     if user_topping != "quit":
#         print(f'We will add {user_topping} topping to your pizza')
#         toppings.append(user_topping)
#         price += 2.5
# print(f'Your pizza will cost {price}')

'''

Exercise 9: Cinemax
A movie theater charges different ticket prices depending on a person's age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Ask a family the age of each person who wants a ticket.

Store the total cost of all the family's tickets and print it out.



'''


# print("Exercise 9")

# user_input = input('Put the age of each person who wants a ticket. Separate the ages with a single space ')

# persons_list= user_input.split(" ")
# total_price = 0
# for i in range(len(persons_list)):
#     persons_list[i] = int(persons_list[i])    
#     if persons_list[i] <=3:
#         ticket_price = 0
#     elif 3 < persons_list[i] <= 12:
#         ticket_price  = 10
#     else:
#         ticket_price  = 15
#     total_price += ticket_price
# print(total_price)

'''
A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
At the end, print the final list.

'''
teen_names = ["John", "Emma", "Sam", "Alex", "Samantha", "Sara"]

user_input = input('Put your age')

for i in teen_names:
    age = int(input('Put your age: '))
    if 16 < age < 21:
        teen_names.remove(i)   
        
print(teen_names)

