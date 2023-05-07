'''
Exercise 1 : Hello World-I Love Python
Instructions
Print the following output in one line of code:
Hello world
Hello world
Hello world
Hello world
I love python
I love python
I love python
I love python

'''
print("Exercise 1")
print("****************************")
print('Hello world\n'*4 + 'I love python\n'*4)
print("****************************")

'''

Exercise 2 : What Is The Season ?
Instructions
Ask the user to input a month (1 to 12).
Display the season of the month received :
Spring runs from March (3) to May (5)
Summer runs from June (6) to August (8)
Autumn runs from September (9) to November (11)
Winter runs from December (12) to February (2)

'''
print("Exercise 2")
print("****************************")

month_number = int(input('Write a month number (1-12): '))

if 3 <= month_number <= 5:
    print(f'{month_number} - It\'s Spring. Spring runs from March (3) to May (5)')
elif 6 <= month_number <= 8:
    print(f'{month_number} - It\'s Summer. Summer runs from June (6) to August (8)')   
elif 9 <= month_number <= 11:
    print(f'{month_number} - It\'s Autumn. Autumn runs from September (9) to November (11)')  
else:
    print(f'{month_number} - It\'s Winter. Winter runs from December (12) to February (2)')
print("****************************")
