matrix_text = '''
    7i3
    Tsi
    h%x
    i #
    sM 
    $a 
    #t%
    ^r!
'''

print(f'Step 0: {matrix_text}')
matrix_text=matrix_text.replace('\n','')
matrix_text=matrix_text.replace('  ','')
print(f'Step 1: {matrix_text}')
matrix_list = []
for i in matrix_text:
    matrix_list.append(i)  
print(f'Step 2: {matrix_list}')
matrix = []
while matrix_list != []:
    matrix.append(matrix_list[:3])
    matrix_list = matrix_list[3:]
print(f'Step 3: {matrix}')

string = ""
for col in range(3):  
    for row in range(len(matrix)):
        if matrix[row][col].isalpha():
            string += matrix[row][col]    
print(f'Step 4: {string}')
