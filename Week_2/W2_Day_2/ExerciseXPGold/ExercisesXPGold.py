'''
Exercise 1: Concatenate Lists.
Write code that concatenates two lists together without using the + sign.
'''
print("Exercise 1")
list_1=[1,2,3,4,5]
list_2=[6,7,8,9,10]
list_1.extend(list_2)
list_3=list_1
print(list_3)
print("****************************")

'''
Exercise 2: Range Of Numbers
Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

'''
print("Exercise 2")

for i in range(1500,2501):
    if i%5==0 and i%7==0:
        print(i)

print()
print("****************************")

'''
Exercise 3: Check The Index
Using this variable

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
Example: if input is 'Cortana' we should be printing the index 1

'''
print("Exercise 3")

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user = input("Wtite your name: ")
if user in names:
    print(names.index(user))
else:
    print("You are not in the list")

print("****************************")

'''
Exercise 4: Greatest Number
Ask the user for 3 numbers and print the greatest number.
    Test Data
    Input the 1st number: 25
    Input the 2nd number: 78
    Input the 3rd number: 87
    The greatest number is: 87

'''
print("Exercise 4")

list_number = []
number_1 = int(input("Input the 1st number: "))
number_2 = int(input("Input the 2st number: "))
number_3 = int(input("Input the 3st number: "))
list_number.extend([number_1, number_2, number_3])
new_list = list_number
max_n = number_1
for i in new_list:
    if i>max_n:
        max_n = i
print(max_n)   
print("****************************")

'''
Exercise 5: The Alphabet
Create a string of all the letters in the alphabet
Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.


'''
print("Exercise 5")
import string
new_string = ''
for i in string.ascii_lowercase:
    new_string +=i
for letter in new_string:
    if letter in 'aeiou':
        print (f'{letter} is vowel' ) 
    else:
        print (f'{letter} is consonant' ) 
print("****************************")

'''
Exercise 6: Words And Letters
Ask a user for 7 words, store them in a list named words.
Ask the user for a single character, store it in a variable called letter.
Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
If the letter doesn't exist in one of the words, print a friendly message with the word and the letter.

'''
print("Exercise 6")

words = input("Input a 7 word, separate them with space: ")
words_list=words.split(" ")
letter = input("Input a letter: ")
for i in range(len(words_list)):
    if letter in words_list[i]:
        for index, value in enumerate(words_list[i]):
            if value==letter:
                print(f'In word "{words_list[i]}" Letter "{value}" has index "{index}"')
    else:
        print(f'There is no letter "{letter}" in word "{words_list[i] }"')

print("****************************")

'''
Exercise 7:
Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.

'''
print("Exercise 7")

long_list = list(range(1, 1000000))
min_num = min(long_list)
max_num = max(long_list)
sum_num = sum(long_list)

print(f'{min_num}, {max_num}, {sum_num}')
print("****************************")


'''
Exercise 8 : List And Tuple
Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
Suppose the following input is supplied to the program: 34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

'''
print("Exercise 8")
input_numbers = input("Input numbers, separate them with coma: ")

list_input_numbers = input_numbers.split(",")

tuple_input_numbers = tuple(list_input_numbers)

print(list_input_numbers)
print(tuple_input_numbers)

print("****************************")

'''
Exercise 9 : Random Number
Ask the user to input a number from 1 to 9 (including).
Get a random number between 1 and 9. Hint: random module.
If the user guesses the correct number print a message that says Winner.
If the user guesses the wrong number print a message that says better luck next time.
Bonus: use a loop that allows the user to keep guessing until they want to quit.
Bonus 2: on exiting the loop tally up and display total games won and lost.

'''
print("Exercise 9")
import random
input_num = None
random_num = random.randrange(0,9)
while input_num!=random_num or input_num != "quit":
    input_num = int(input("Input a numbers from 0 to 9: "))
    if input_num==random_num:
        print("You are a winner!")
        break
    else:
        print("Better luck next time.")
print("****************************")
