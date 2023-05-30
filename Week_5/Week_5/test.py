people_list = [
    {
    "id": 1,
    "name": "Bob Smith",
    "age": 35,
    "country": "USA"
    },
    {
    "id": 2,
    "name": "Martha Smith",
    "age": 60,
    "country": "USA"
    },
    {
    "id": 3,
    "name": "Fabio Alberto",
    "age": 18,
    "country": "Italy"
    },
    {
    "id": 4,
    "name": "Dietrich Stein",
    "age": 85,
    "country": "Germany"
    }
] 

def age_sorted(x):
    return x['age'] 
sorted_people_list = sorted(people_list, key = age_sorted)
for person in sorted_people_list:
    print(person['id'], person['name'], person['age'], person['country'])
print(sorted_people_list)