text = "without,hello,bag,world"
text_list = text.split(",")
text_list.sort()
print(text_list)
new_text = ", ".join(text_list)
print(new_text)       
    

