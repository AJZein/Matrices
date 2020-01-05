def matrix_maker():
    matrix_dict = {}
    k = 1
    n = int(input("How many matrices would you like to create: "))
    while k <= n:
        key = input("Name of this matrix: ")
        print("Number of rows in matrix", key, ": ", end="")
        r = int(input())
        print("Number of columns in this matrix", key, ": ", end="")
        c = int(input())
        k += 1
        matrix = [[0 for x in range(c)] for y in range(r)]
        for i in range(r):
            for j in range(c):
                print("Entry", i, j, ": ", end="")
                matrix[i][j] = int(input())
        matrix_dict[key] = matrix
    return matrix_dict

def adder(A = 0, B = 0):
    if not A or not B:
        A = matrix_dict[input("Name of the first matrix to add: ")]
        B = matrix_dict[input("Name of the second matrix to add: ")]
    if len(A) != len(B) or len(A[1]) != len(B[1]):
        return "Undefined"
    a = float(input("Scalar multiple of the first matrix: "))
    b = float(input("Scalar multiple of the second matrix: "))
    i = 0
    j = 0
    r = len(A)
    c = len(A[1])
    C = [[0 for x in range(c)] for y in range(r)]
    while i != r:
        while j != c:
            C[i][j] = a*A[i][j] + b*B[i][j]
            j += 1
        i += 1
        j = 0
    return C

def printer(matrix = 0):
    if not matrix:
        matrix = matrix_dict[input("Which matrix would you like to print: ")]
    elif matrix == "Undefined":
        return print("Your matrix is undefined")
    r = len(matrix)
    c = len(matrix[1])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], "",end="")
        print("\n")

def multiplier(A=0, B=0):
    if not A or not B:
        A = matrix_dict[input("Name of the first matrix to multiply: ")]
        B = matrix_dict[input("Name of the second matrix to multiply: ")]
    if len(A[1]) == len(B):
        r = len(A)
        c = len(B[1])
        C = [[0 for x in range(c)] for y in range(r)]
        i = 0
        j = 0
        while i != r:
            while j != c:
                for n in range(0, len(B)):
                    C[i][j] += A[i][n]*B[n][j]
                j += 1
            i += 1
            j = 0
        return C
    else:
        return "Undefined"

def transpose(A=0):
    if not A:
        A = matrix_dict[input("Which matrix would you like to find the transpose of: ")]
    r = len(A)
    c = len(A[1])
    B = [[0 for x in range(c)] for y in range(r)]
    i = 0
    j = 0
    while i != r:
        while j != c:
            B[j][i] = A[i][j]
            j += 1
        i += 1
        j = 0
    return B

def cofactor2(A=0):
    if not A:
        A = matrix_dict[input("Which matrix would you like to convert into cofactors: ")]
    
    

def determinant2(A=0):
    if not A:
        A = matrix_dict[input("Which matrix would you like to calculate the determinant of: ")]
    det = A[1][1]*A[2][2] - A[1][2]*A[2][1]
    return det
    
    
matrix_dict = matrix_maker()
Help = ("""Here are your options.
           Typing add will allow you to add matrices.
           Typing multiply will allow you to multiply matrices
           Typing print will allow you to print a matrix
           Typing data will allow you to create new matrices
           Typing transpose will allow you to calculate the transpose of a matrix""")
print(Help)
user_choice = input()
while user_choice:
    user_choice = user_choice.lower()
    
    if user_choice == "add":
        Add1 = adder()
        printer(Add1)
        if Add1 != "Undefined":
            print("Type a name to give to this new matrix")
            matrix_dict[input()] = Add1
        
    elif user_choice == "multiply":
        Multiply1 = multiplier()
        printer(Multiply1)
        if Multiply1 != "Undefined":
            print("Type a name to give to this new matrix")
            matrix_dict[input()] = Multiply1
    elif user_choice == "transpose":
        Transpose1 = transpose()
        printer(Transpose1)
        print("Type a name to give to this new matrix")
        matrix_dict[input()] = Transpose1
        
    elif user_choice == "print":
        printer()
        
    elif user_choice == "data":
        matrix_dict = matrix_maker()
        
    elif user_choice == "help":
        print(Help)
        
    else:
        print("Please enter a valid function. Try typing help for a list of functions.")
    user_choice = input("Type a new function to perform or press enter to exit\n")

    
 

