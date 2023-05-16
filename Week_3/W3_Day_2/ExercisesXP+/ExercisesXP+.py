# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)

# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.

print('ExerciseXP+ 1')
class Family ():
    def __init__(self, last_name):
        self.last_name = last_name
        self.members_list =[
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
            ]
            
    def born(self, **child):       
        self.members_list.append(child)
        print('Congratulating! You have a child')
        print(self.members_list)
    
    def is_18(self, family_member):
        for member in self.members_list:
            if member["name"]==family_member :
                if member["age"]>18:
                    return True
                else :
                    return False

    def family_presentation(self):
        string = f'Family {self.last_name}. Members: '
        for member in self.members_list:
            name = member['name']
            string +=' ' + name
        print(string)

class TheIncredibles (Family):
    def __init__(self, last_name):
        super().__init__(last_name)
        self.members =[
            {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'}, 
            
            {'name':'Sarah','age':32,'gender':'Female','is_child':False, 'power': 'read minds','incredible_name':'SuperWoman'}
            ]
        
    
    def use_power(self, firstname):
        age = super().is_18(firstname)
        if age:
            for member in self.members:
                if member['name'] == firstname:
                    print(member['power'])

    def incredible_presentation(self):
        super().family_presentation()
        string_power = ''
        for member in self.members:
            incredible_name=member['incredible_name']
            power = member['power']
            string_power += ' '+ incredible_name + ' has a power ' + power
        print(string_power)


family_1 =Family('Smith')
family_1.born(name='Alex',age=0, gender='Male', is_child=True)
family_1.is_18('Sarah')
family_1.family_presentation()


family_2 =TheIncredibles('Jons')
family_2.born(name='Jack',age=0, gender='Male', is_child=True)
family_2.family_presentation()
family_2.use_power("Sarah")
family_2.born(name='Jack',age=0, gender='Male', is_child=True, power = 'Unknown Power')
family_2.incredible_presentation()