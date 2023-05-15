'''
Challenge 1
Ask a user for a word
Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

Make sure the letters are the keys.
Make sure the letters are strings.
Make sure the indexes are stored in a list and those lists are values.
Examples

"dodo" ➞ { "d": [0, 2], "o": [1, 3] }

"froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

"grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}

'''
print("Challenge 1")
# check again your output. It is not as the exercise is aking to do. 
# I am pretty sure you will get it fast, so I wont say what is the problem. Please come to me if you need help ;)
word = input("Write a word: ")
list_index = [num for num in range(len(word))]
my_dictionary = dict(zip(word, list_index))
print(my_dictionary )

print("Challenge 2")
store = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1000",
  "Fertilizer": "$20",
  "Apple" : "$4",
  "Fan": "$14",
  "Pan": "$100",
  "Spoon": "$2"
}

store = {key: value.replace("$", " ") for key, value in store.items()}

store = {key: int(value) for key, value in store.items()}

wallet = int(input("How much money do you have: "))
can_buy = []
for key, value in store.items():
  if value < wallet:
      can_buy.append(key)
      wallet -=value
if can_buy:
  can_buy.sort()
  print(f'You can buy: {can_buy}')
  
else:
  print("You can buy: Nothing")
  
