'''
Here is a table of prices for a wedding catering company:
# of guests	price
Up to 50 people	$4,000
Up to 100 people	$10,000
Up to 200 people	$15,000
More than 200 people	$20,000

📝 Instructions:

Please write an program that prompts the user for the number of people attending their wedding and prints the corresponding price in the console.
For example, if the user says that 20 people are attending to the wedding, it must cost $4,000 dollars.
'''
amount_of_people = int(input("How many people: "))

if amount_of_people <= 50:
    print('it must cost $4,000 dollars')
elif  50 <= amount_of_people <= 100:
    print('it must cost $10,000 dollars')
    
elif  100 <= amount_of_people <= 200:
    print('it must cost $15,000 dollars')
    
else:
    print('it must cost $20,000 dollars')