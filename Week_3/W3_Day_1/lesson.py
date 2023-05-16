# class Dog :

#     def __init__(self, name_dog, age_dog, dog_energy = 100) :
#         self.name = name_dog
#         self.age = age_dog
#         self.energy =  dog_energy

#     def bark(self):
#         print(f"{self.name} said Wouaf Wouaf")

#     def play(self, type_game="stick"):
#         if self.energy < 10 :
#             self.sleep()
#         else : 
#             if type_game == "ball":
#                 self.energy -= 10
#             elif type_game == "stick":
#                 self.energy -= 5
#             else :
#                 self.energy -= 2
    
#     def play_with_other_dog(self, other_dog) :
#         #other_dog is an object
#         # print(other_dog.__dict__)
#         print(f"{self.name} is playing with {other_dog.name}")
#         self.energy -= 70
#         other_dog.energy -= 50
    
#     def sleep(self) :
#         self.energy += 50


# tom_dog = Dog("King", 7)
# # tom_dog is an object of the Dog class
# # tom_dog is an instance of the Dog class
# lea_dog = Dog("Rex", 4)
# lea_dog.bark()
# lea_dog.play()

# tom_dog.play_with_other_dog(lea_dog)

# print(f"{tom_dog.name} energy is {tom_dog.energy}")
# print(f"{lea_dog.name} energy is {lea_dog.energy}")

class Employee():
    def __init__(self, firstname, lastname, age, job, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
    # def __add__(self):
    #     string = f'{self.firstname} + {self.lastname}'
    #     return string
    
    def __gt__(employee1, employee2):
        if employee1.salary > employee2.salary:
            result =employee1.salary
        else:
            result = employee2.salary
        return result
    
    def __str__(self):
        string = f'I\'m {self.firstname} {self.lastname}'
        return string
    
    def eemployee_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old {self.job} {self.salary}'
    
    def get_fullname(self):
        return self.firstname + " " + self.firstname
    
    def happy_birthday(self) : 
        return self.age+1
        
    def get_promotion(self, promotion_amount): 
        return self.salary + promotion_amount
    
employee_1 = Employee('Lea', 'Smith', 30,'developer', 30000)

employee_2 = Employee('David', 'Schartz', 20, 'project manager', 20000)

print(employee_1)
print(employee_2)
print(employee_1 > employee_2)
print(employee_1.get_fullname())
print(employee_1.happy_birthday())

# print(employee_1.eemployee_info())
# print(employee_2.eemployee_info())

# print(employee_1.get_fullname())
# print(employee_2.get_fullname())

# print(employee_1.happy_birthday())
# print(employee_2.happy_birthday())

# print(employee_1.get_promotion(20))
# print(employee_2.get_promotion(15))
