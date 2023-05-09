'''
Challenge 1
Ask the user for a number and a length.
Create a program that prints a list of multiples of the number until the list length reaches length.
'''
user_input = input("Write number and length of list. Separate by space ")
user_list = user_input.split(" ")

number = int(user_list[0])
length = int(user_list[1])

result_list = []

for i in range(length):
    number = number *(i+1)
    result_list.append(number)
    number = int(user_list[0])
print( result_list)

'''
Challenge 2
Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
'''
user_string = input("Write something ")
letter = ''
new_string =''
for i in user_string:
    if i !=letter:
        new_string = new_string + i
    letter = i

print(new_string)