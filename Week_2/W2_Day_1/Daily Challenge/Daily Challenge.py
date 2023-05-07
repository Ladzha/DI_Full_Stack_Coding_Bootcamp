'''
Daily Challenge: Build Up A String
1.  Using the input function, ask the user for a string. The string must be 10 characters long.
If it's less than 10 characters, print a message which states “string not long enough”.
# If it's more than 10 characters, print a message which states “string too long”.

2.  Then, print the first and last characters of the given text.

Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
The user enters "Hello World"
Then, you have to construct the string character by character
H
He
Hel
etc
Hello World

4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
Hlrolelwod
'''

user_string = input('Write string in 10 letters: ')

if len(user_string) == 10:
    print('Perfect string')
elif len(user_string)< 10:
    print('String not long enough')
    
elif len(user_string)> 10:
    print('String too long')
    

print('Fist characters of the text: ' + user_string[0])
print('Last characters of the text: ' + user_string[-1])

result = ""
if user_string == "Hello World":  
    for n in user_string:
        result += n
        print(result)