# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension


text = "without,hello,bag,world,all"
text = input("Write wors separated by coma, no space: ")
text_list = text.split(",")
text_list.sort()
new_text = ",".join([word for word in text_list])
print(new_text)       