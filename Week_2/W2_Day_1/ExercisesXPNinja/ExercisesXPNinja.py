'''
Exercise 3 : Outputs
Instructions
Predict the output of the following code snippets:
3 <= 3 < 9 Result: True
3 == 3 == 3 Result:  True
bool(0) Result: False
bool(5 == "5") Result: False
bool(4 == 4) == bool("4" == "4") Result: True
bool(bool(None)) Result: True
x = (1 == True) Result: 1
y = (1 == False) Result: 0
a = True + 4 Result: 5
b = False + 10 Result: 0

print("x is", x) Result: x is True
print("y is", y) Result: x is False
print("a:", a) Result: a: 5
print("b:", b) Result: b: 10


Exercise 4 : How Many Characters In A Sentence ?
'''
print("****************************")
print("Exercise 4")
my_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''
print(len(my_text))
print("****************************")

'''
Exercise 5: Longest Word Without A Specific Character
Keep asking the user to input the longest sentence they can without the character “A”.
Each time a user successfully sets a new longest sentence, print a congratulations message.
'''
print("Exercise 5")

longest_word_length = 0

i = 1
while i < 8:
    user_sentence = input('Input the longest sentence you can without the character “A”: ')

    a_amount = user_sentence.find("A")

    if a_amount>-1:
        print(f'Teire is "A". Try again!')
    elif a_amount == -1:
        user_sentence_length = len(user_sentence)
        
        if user_sentence_length > longest_word_length:
            longest_word_length = user_sentence_length
            print(f'Congratulations! This sentence {user_sentence} is the longest: there are {longest_word_length} characters')
            
        else:
            print(f'This sentence {user_sentence} is NOT the longest. Try again!')

    print("****************************")
    i += 1
print("Fin")
print("****************************")