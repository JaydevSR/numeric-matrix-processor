from matrix import Matrix

def menu():
    print("""Choices:
            1. Add matrices
            2. Multiply matrix by a constant
            3. Multiply matrices
            4. Transpose matrix
            5. Calculate a determinant
            6. Inverse matrix
            0. Exit""")
    choice = input("Your choice:")

    if choice == "1":
        mat1 = Matrix()
        mat2 = Matrix()
        res = mat1.add_mat(mat2)
        Matrix.print_result(res)
        
    elif choice == "2":
        mat1 = Matrix()
        scalar = float(input("Enter scalar: "))
        res = mat1.scalar_mult(scalar)
        Matrix.print_result(res)
      
    elif choice == "3":
        mat1 = Matrix()
        mat2 = Matrix()
        res = mat1.mat_mult(mat2)
        Matrix.print_result(res)
        
    elif choice == "4":
        print("""Planes:
                1. Main diagonal
                2. Side diagonal
                3. Vertical line
                4. Horizontal line""")
        plane = int(input("Your choice:"))
        mat1 = Matrix()
        res = mat1.transpose(plane)
        Matrix.print_result(res)
    
    elif choice == "5":
        mat1 = Matrix()
        res = Matrix.determinent(mat1.mat, mat1.size)
        Matrix.print_result(res)
        
    elif choice == "6":
        mat1 = Matrix()
        res = mat1.invert()
        Matrix.print_result(res)
        
    elif choice == "0":
        return False
        
    else:
        print("Unknown Input!")
    return True