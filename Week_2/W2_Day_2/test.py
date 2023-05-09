# print("Exercise 1")
# my_fav_numbers = {1, 2, 3, 4, 5, 6}
# print('my favorites numbers: ', my_fav_numbers)
# my_fav_numbers.append(7)
# my_fav_numbers.insert(0, 8)
# print('my favorites numbers + adding numbers: ' , my_fav_numbers)
# my_fav_numbers.pop()
# print('my favorites numbers - last: ' , my_fav_numbers)
# friend_fav_numbers = {7, 8, 9, 10, 11, 12}
# print('my friend favorites numbers: ' , friend_fav_numbers)
# our_fav_numbers=my_fav_numbers+friend_fav_numbers
# print('our favorites numbers: ' , our_fav_numbers)

# print("****************************")

print("Exercise 3")

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print("Basket list", basket)
basket.remove("Banana")
basket.remove("Blueberries")
print("Basket List - banana and Blueberries", basket)
basket.append("Kiwi")
basket.insert(0, "Apples")
print("Basket List + kiwi and apples", basket)
apples_number=basket.count("Apples")
print(f"There are {apples_number} apples in the basket")
basket.clear()
print("Empty basket", basket)
print("****************************")


print("Exercise 7")

fruits = input("What is your favorite fruits? Separate the fruits with a single space")
fruits_list = fruits.split()
print("Input a name of any fruit")
print('You chose one of your favorite fruits! Enjoy!')

print('You chose a new fruit. I hope you enjoy')

print("****************************")


print("Exercise 9")

family_members_age = "50 2 3 7 12 "
# family_members_age = input('Put the age of each person who wants a ticket. Separate the ages with a single space')

persons_list=family_members_age.split(" ")
print(family_members_age)

# if age <=3:
#     price = 0
# elif 3 < age <= 12:
#     price = 10
# else:
#     price = 15




print("Exercise 10")

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

finished_sandwiches = []

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f'I made your {sandwich}')

print("Exercise 11")

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
sandwich_orders.extend(["Pastrami sandwich","Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich"])

print("The deli has run out of pastrami")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f'I made your {sandwich}')