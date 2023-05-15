print("Exercise 1")

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

numbers_name = dict(zip(keys, values))
print(numbers_name)


print("Exercise 2")

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
age = 0
total_cost=0
for name, age in family.items():
    int(age)    
    if age < 3:
        price = 0
    elif 3 < age < 12:
        price = 10
    else:
        price = 15
    total_cost +=price 
    print(f'{name} is {age}, your ticket costs {price}')
print(f'Pay {total_cost} $')

# Bonus:

new_family = {}
total_cost=0
length = int(input('How many people: '))
for item in range(length):
    new_name = input('Enter your name: ')
    new_age = int(input('Enter your age: '))
    new_family[new_name] = new_age
print(f'Your family {new_family}')

for person_name, person_age in new_family.items():
    if person_age < 3:
        price = 0
    elif 3 < person_age < 12:
        price = 10
    else:
        price = 15
    total_cost +=price 
    print(f'{person_name} is {person_age}, your ticket costs {price}')
print(f'Pay {total_cost} $')
print("****************************")

print("Exercise 3")

brand = {
    "name": "Zara",
    "creation_date" : "1975",
    "creator_name" : "Amancio Ortega Gaona ",
    "type_of_clothes" : ["men", "women", "children", "home"],
    "international_competitors" : ["Gap", "H&M", "Benetton"],
    "number_stores" : "7000",
    "major_color:" : {"France" : "blue", "Spain": "red", "US": ["pink", "green"]}
    }
brand["number_stores"] =2

clients = brand["type_of_clothes"]
clients.pop()
client_str = ""
for client in clients:
    client_str += client + " "
print(f"Zaras clients are: {client_str}")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
brand.pop("creation_date")  
print(brand)
print(brand["international_competitors"][-1])
print(f'Major_color in US: {brand["major_color:"]["US"]}')
print("Length of the dictionary: ", len(brand))

for key in brand.keys():
    print(key)
more_on_zara = brand.copy()
more_on_zara["creation_date"] = "1975"
more_on_zara["number_stores"] = "10 000"
brand.update(more_on_zara)
print(f'Dictionary brand: {brand}')
print(f'Dictionary brand: {more_on_zara}')
print(brand["number_stores"])
print("****************************")

print("Exercise 4")
#In step4.1 - You are adding Ronald - name without i.
users = ["Mickey","Minnie","Ronald","Ariel","Pluto"]

values_a = []
for i in range(len(users)):
    values_a.append(i)
    i+=1
disney_users_A = dict(zip(users, values_a))
print(disney_users_A)

values_b = []
for i_b in range(len(users)):
    values_b.append(i_b)
    i_b+=1
disney_users_A = dict(zip(values_b, users))
print(disney_users_A)

values_c = []
users_sort = ["Mickey","Minnie","Donald","Ariel","Pluto"]
users_sort.sort()
for i_c in range(len(users_sort)):
    values_c.append(i_c)
    i_c+=1
disney_users_C = dict(zip(users_sort, values_c))
print(disney_users_C) 

values_a = []
for i in range(len(users)):
    if "i" in users[i]: 
        values_a.append(i)
        i+=1
        continue
disney_users_A = dict(zip(users, values_a))
print(disney_users_A)

disney_users_A = {}
for index, item in enumerate(users):
    if item[0].lower() in "mp":
        disney_users_A[item] = index
print(disney_users_A)
