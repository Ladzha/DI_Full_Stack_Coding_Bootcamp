# print('Exercise 1')

# def abs_ex(a: int):
#     '''
#     Return absolute value   
#     '''
#     print(abs(a))

# abs_ex(-9)
# print(abs_ex.__doc__)

# def int_ex(a:str):
#     '''
#     Convert string to integer  
#     '''
#     print(int(a))

# int_ex('9')
# print(int_ex.__doc__)

# def input_ex():
    
#     '''
#     Get data from user
    
#     '''
#     result = input('Write a negative number: ')
#     print(result)

# input_ex()
# print(input_ex.__doc__)

print('***************')

print('Exercise 2')
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
        
    def __str__(self):
        print(f'{self.amount} {self.currency}')
        return f'{self.amount} {self.currency}'
        
    def str(self):
        self.__str__(self)      
            
    def int(self):
        num = int(self.amount)
        return num
    
    def repr (self):
        self.__repr__(self)
        
    #Your code starts HERE 
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

str(c1)
int(c1)
# repr(c1)
# c1 + 5
# c1 + c2
# print(c1) 
# print('***************')