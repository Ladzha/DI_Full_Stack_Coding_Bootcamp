# Cant Install 

# I dont know it doesn't work Exercise 7
# Faker module  Exercise 9 



# 🌟 Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

import random
def get_number():
    number = random.randint(1,100)
    user_num = int(input('Write a number: '))
    if number==user_num:
        print('Success!')
    else:
        print(f'No! My number is {number}!')

get_number()

# 🌟 Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

import string
def get_random_string():
    random_string = ' '.join(random.choices(string.ascii_letters, k=5)) 
    print(random_string)
    
get_random_string()

# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.


import datetime

def display_date():
    date=datetime.date.today()
    print(date)
display_date()

# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).


def until_january():
    date_today=datetime.datetime.now()
    January_1 = datetime.datetime(year=2024, month=1, day=1, hour=0, minute=0, second=0)
    time_until=January_1-date_today
    string =  f'The 1st of January is in {time_until}'
    print(string)
until_january()


# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.


def life_in_minutes(birthday):
    date_today =datetime.datetime.now()
    birth_date = datetime.datetime.strptime(birthday, '%Y-%m-%d')
    days_until = date_today-birth_date
    minutes= round(int(days_until.total_seconds())/60)
    message =  f'You live {minutes} minutes'
    print(message)
life_in_minutes('1973-11-28')

# Exercise 7 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

import holidays 


def upcoming_holiday():
    # us_holidays = holidays.country_holidays('US')

    date_today=datetime.date.today()
    upcoming_holiday=None
    
    us_holidays = holidays.US() 
    us_holidays = holidays.country_holidays('US')


    
    for date, name in us_holidays.items():
        if date >= date_today:
            upcoming_holiday = date
            break
        
    if upcoming_holiday:      
        time_until = upcoming_holiday-date_today
    
        string =  f'The next holiday is {name} in {time_until}'
        
        print(date_today)
        print(string)

upcoming_holiday()

# Exercise 8 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.

def old_on_planet():
    planets = {
        'Earth': 1,
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }
    
    date_today=datetime.datetime.now()
    birth_date = datetime.datetime(year=1981, month=8, day=17, hour=0, minute=0, second=0)
    age=date_today-birth_date
    seconds_age= float(age.total_seconds())  
    earth_age = round(seconds_age/31557600) 
    for key, value in planets.items():
        you_age = earth_age/value
        result = f'On {key} you are {you_age}.'
        print(result)
    
old_on_planet()

from faker import Faker
fake = Faker()
   
users =[]
def fake_user():  
    user={
        'name': fake.name(), 
        'address': fake.address(), 
        'language_code': fake.language_code()
        }
    users.append(user)
fake_user()
fake_user()
fake_user()
fake_user()

for user in users:
    print(user)