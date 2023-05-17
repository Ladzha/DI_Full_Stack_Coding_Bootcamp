import string
import random
import requests
import json 

# 🌟 Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.


def get_random_string():
    user_input = int(input("How long the string should be: "))
    random_string = ' '.join(random.choices(string.ascii_letters, k=user_input)) 
    print(random_string)  
get_random_string()

def get_words_from_file():
    with open("words.txt", "r") as words:
        words_list = words.read().split()
        return words_list
get_words_from_file()

def get_random_sentence(length):
    words_list=get_words_from_file()
    random_list = random.choices(words_list, k=length)
    random_string = ' '.join(random.choices(words_list, k=length)) 
    # print(random_list)
    # print(random_string)
    print(random_string.lower())   
get_random_sentence(3)

def main():
    print('This programm create random a sentence. You put a number of word and program create a sentence')
    while True:
        try: 
            user_input = int(input("How long the sentence should be from 2 to 20: "))
        
            if 2 <= user_input <= 20:
                break   
            else:
                print('Invalid number')
        
        except ValueError as error:
            print('Not a number')
            print(error)    
    get_random_sentence(user_input)    
main()


    
# import json
# sampleJson = """{ 
# "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

