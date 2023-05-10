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
word = input("Write a word: ")
list_index = [num for num in range(len(word))]
my_dictionary = dict(zip(word, list_index))
print(my_dictionary )


# store = {
#   "Water": "1",
#   "Bread": "3",
#   "TV": "1,000",
#   "Fertilizer": "20",
#   "Apple" : "4",
#   "Fan": "14",
#   "Pan": "100",
#   "Spoon": "2"
# }
# wallet = 30
# # price_item = 0
# can_buy = []
# for i in store.values():
#     if int(i) < wallet:
#         can_buy.append(store)
#         wallet -=i
# print(can_buy)


