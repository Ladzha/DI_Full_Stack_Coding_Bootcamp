# def colorize(text, color):
#     colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
#     print(text)
    
#     try: 
#         if color not in colors:
#             raise ValueError('No color in tuple') 
#         if type(text) !=str:
#             print(color) 
#             raise TypeError ('Not string type')
#     except Exception as error:
#         print(error)
      
# colorize("hello", "cyan")
# colorize(123, "red")
# colorize("hello", "red")

import json
user = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "email" : None,
    "children": [
        {
            "firstName": "Alice",
            "age": 6,
            "loves_school" : True
        },
        {
            "firstName": "Bob",
            "age": 8,
            "loves_school" : False
        }
    ]
}

my_json=json.dumps(user)
print(my_json)

person_str = {'user':'john', 'age':'35'}
# person_dict = json.loads(person_str)
# print(person_str)

import requests

# response=requests.get('http://api.open-notify.org/iss-now.json')

# print(dir(response))
# print(response.status_code)
# print(response.content)
# info=json.loads(response.content)
# info=response.json()
# print(info)

# latitude = info['iss_position']['latitude']
# longitude = info['iss_position']['longitude']

# sentence = f'the ISS in qt latitued {latitude} and longitude {longitude}'

# print(sentence)
import json
import requests
# parameters = {'limit':2}
# response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu', params = parameters)


# info=response.json()
# print(info['results'])


# {'timestamp': 1684399958, 'iss_position': {
#     'latitude': '3.4531', 'longitude': '-75.3703'
#     }, 
#  'message': 'success'}

