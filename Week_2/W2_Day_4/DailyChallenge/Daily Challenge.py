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
matrix_text = matrix_text.replace("\n", "")
matrix_list = []
for simbol in matrix_text: 
    if simbol !=' ':
        matrix_list.append(simbol)
print(f'Step 1: {matrix_list}')
matrix = []
string = ""
while matrix_list != []:
    matrix.append(matrix_list[:3])
    matrix_list = matrix_list[3:]
print(f'Step 2: {matrix}') 

for j in range(3):
    for i in range(len(matrix)):
        if matrix[i][j].isalpha():
            string += matrix[i][j]
        # else:
        #     string += " "
print(f'Step 3: {string}')

