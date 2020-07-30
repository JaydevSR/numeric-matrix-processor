#Matrix class 

class Matrix:
    def __init__(self):
        size = list(map(int, input("Enter matrix size:").split(" ")))
        if len(size) > 2:
            raise Exception("ERROR: only two dimentional matrices allowed.")
        else:
            self.size = size
            print("Enter matrix:")
            self.mat = [list(map(float, input().split(" "))) for i in range(self.size[0])]
        
    @staticmethod
    def print_result(result):
        if isinstance(result, list):
            result = "\n".join([" ".join(row) for row in result])
            print(f"The result is:\n{result}")
        else:
            print(result)
        
    @staticmethod 
    def cofactor(mat, size, elem):
        r, c = size
        a, b = elem
        rem_mat = [[mat[i][j] for j in range(c) if j != b] for i in range(r) if i != a]
        minor = Matrix.determinent(rem_mat, [r - 1, c - 1])
        res = (-1)**(a + b) * minor
        return res
        
    @staticmethod    
    def determinent(mat, size):
        r, c = size
        if r != c:
            print("Inavalid: Determinent can't be calculated for a non-square matrix.")
            return
        if (r, c) == (1, 1):
            return mat[0][0]
        return sum([mat[i][0] * Matrix.cofactor(mat, size, [i,0]) for i in range(r)])
        
    def invert(self):
        mat = self.mat
        r, c = self.size
        det = Matrix.determinent(mat, [r, c])
        if det == 0:
            print("No Inverse: Singular Matrix")
        else:
            inverse = [[str(round(Matrix.cofactor(mat, [r,c], [i,j]) / det, 4)) for i in range(r)] for j in range(c)]
            return inverse
        
    def scalar_mult(self, scalar):
        r, c = self.size
        result = [[str(scalar*int(self.mat[i][j])) for j in range(c)] for i in range(r)]
        return result
        
    def add_mat(self, other):
        if self.size != other.size:
            print("Size Mismatch: The operation cannot be performed.")
            return
        else:
            r, c = self.size
            mat1, mat2 = self.mat, other.mat
            result = [[str(mat1[i][j] + mat2[i][j]) for j in range(c)] for i in range(r)]
            return result
        
    def mat_mult(self, other):
        ra, ca, rb, cb = *self.size, *other.size
        mat1, mat2 = self.mat, other.mat
        if ca != rb:
            print("Size Mismatch: The operation cannot be performed.")
            return
        else:
            result = [[str(sum([mat1[i][k]*mat2[k][j] for k in range(ca)])) for j in range(cb)] for i in range(ra)]
            return result

    def transpose(self, plane):
        r , c = self.size
        if plane == 1:
            result = [[str(self.mat[i][j]) for i in range(r)] for j in range(c)]
            return result
        elif plane == 2:
            result = [[str(self.mat[r-1 - i][c-1 - j]) for i in range(r)] for j in range(c)]
            return result
        elif plane == 3:
            result = [map(str, row[::-1]) for row in self.mat]
            return result
        elif plane == 4:
            result = [map(str, row) for row in self.mat[::-1]]
            return result
        else:
            print("Unknown Plane of transpose.")
            return
