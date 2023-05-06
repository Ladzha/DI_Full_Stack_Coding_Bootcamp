'''
Exercise 1 : Hello World
Print the following output in one line of code:
Hello world
Hello world
Hello world
Hello world
'''
print("Exercise 1")
print('Hello world \nHello world \nHello world \nHello world')
print("****************************")
'''
Exercise 2 : Some Math
Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
'''
print("Exercise 2")
print(99**3*8)
print("****************************")
'''
Exercise 3 : What Is The Output ?
Predict the output of the following code snippets:
5 < 3               False
3 == 3              True
3 == "3"            False
"3" > 3             Error
"Hello" == "hello"  False
'''
print("Exercise 3")
print(bool(5 < 3))
print(bool(3 == 3))
print(bool(3 == "3"))
#print(bool('3' > 3 ))
print(bool("Hello" == "hello"))
print("****************************")

'''
🌟Exercise 4 : Your Computer Brand
Create a variable called computer_brand which value is the brand name of your computer.
Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
'''
print("Exercise 4")
computer_brand = "HP"
print('I have a', computer_brand, 'computer')
print("****************************")
'''
🌟 Exercise 5 : Your Information
Create a variable called name, and set it's value to your name.
Create a variable called age, and set it's value to your age.
Create a variable called shoe_size, and set it's value to your shoe size.
Create a variable called info and set it's value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
Have your code print the info message.
Run your code
'''
print("Exercise 5")
name = "Alla"
age = 36
shoe_size = 7
info = 'I am still', name, "I'm", age, 'years old. My shoe size is', shoe_size
print(info)
print("****************************")
'''
🌟 Exercise 6 : A & B
Create two variables, a and b.
Each variable value should be a number.
If a is bigger then b, have your code print Hello World.
'''
print("Exercise 6")
a=7
b=5

if a>b:
    print("Hello world")
print("****************************")

'''
Exercise 7 : Odd Or Even
Write code that asks the user for a number and determines whether this number is odd or even.
'''
print("Exercise 7")
number = input("Write a number: ")
number = int(number)
result = number % 2
if result == 0:
    print('The number is even')
else:
    print('The number is odd')
print("****************************")
'''
🌟 Exercise 8 : What's Your Name ?
Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
'''
print("Exercise 8")
my_name ="Alla"
user_name = input("Write your name: ")
if my_name == user_name:
    print('Wow we have the same name')
else:
    print('Oh no we have different names')
print("****************************")
    
'''
🌟 Exercise 9 : Tall Enough To Ride A Roller Coaster
Write code that will ask the user for their height in inches.
If they are over 145cm print a message that states they are tall enough to ride.
If they are not tall enough print a message that says they need to grow some more to ride.
'''
print("Exercise 9")
height = input('Write your height in inches: ')
height = float(height)*2.54
print("Your height is ", height, "cm")

if height > 145.0:
    print("You are tall enough to ride a Roller Coaster")

elif height < 145.0:
    print("You need to grow some more to ride a Roller Coaster")
print("****************************")