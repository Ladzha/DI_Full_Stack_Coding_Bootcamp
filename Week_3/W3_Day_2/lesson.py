class Employee :
    def __init__(self, emp_fn, emp_ln, emp_age, emp_job, emp_salary) :
        self.firstname = emp_fn
        self.lastname = emp_ln
        self.age = emp_age
        self.job = emp_job
        self.salary = emp_salary

    def get_fullname(self) :
        fullname = self.firstname + " " + self.lastname
        return fullname
    
    def happy_birthday(self) : 
        self.age += 1
    
    def get_promotion(self, promotion_amount) :
        self.salary += promotion_amount

    def show_employee(self) :
        print(f"{self.firstname} {self.lastname} {self.age} {self.job} {self.salary}")
     
class Developer(Employee) :
    def __init__(self, emp_fn, emp_ln, emp_age, emp_job='Developer' , emp_salary=15000) :
        super().__init__(emp_fn, emp_ln, emp_age, emp_job, emp_salary)
        self.skills_list = []   
    def add_skills(self, *skills):
        for skill in skills:
            self.skills_list.append(skill)
        print(self.skills_list)
        
    def coding(self):
        string = f'a nice sentence with the'
        for skill in self.skills_list:
            string += ' '+ skill + ' '
        print(string)
        #or sentence = ''.join(self.skills_list)
    def coding_with_partner(self, other_developer) : 
        print (f'a nice sentence with the {self.firstname} and {other_developer.firstname}, and {" , ".join(self.skills_list)} and {other_developer.skills_list}')
      
employee1=Developer('Tom', 'Cruiz', 30)
employee2=Developer('Angelina ', 'Jolie ', 23)
employee2.add_skills('Python', 'Java', 'C#')
employee1.add_skills('Point', 'JavaSkript', 'C++')
employee1.coding()
employee1.coding_with_partner(employee2)
