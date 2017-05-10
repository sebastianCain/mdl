
from draw import *
import random
#class Transform:
'''
IDEN_MTRX = [[1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]]
'''

# BASIC MATRIX STUFF

def identity_mtrx():
    matrix = []
    for i in range(4):
        line = []
        for j in range(4):
            if i == j:
                line.append(1)
            else:
                line.append(0)
        matrix.append(line)
    return matrix

def hermite_mtrx():
    return [[ 2, -3,  0,  1],
            [-2,  3,  0,  0],
            [ 1, -2,  1,  0],
            [ 1, -1,  0,  0]]

def bezier_mtrx():
    return [[-1,  3, -3,  1],
            [ 3, -6,  3,  0],
            [-3,  3,  0,  0],
            [ 1,  0,  0,  0]]
 
def scalar_mult(mtrx, scalar):
    for i in range(len(mtrx)):
        for j in range(len(mtrx[0])):
            mtrx[i][j] *= scalar
    return mtrx

def mtrx_mult(m1, m2):
    m3 = []
    
    for i in range(len(m1)):
        #this is for each array in m1
        line = []
        for j in range(len(m2[0])):
            #each run of the following block is for one entry in the resultant matrix, i.e. 4*N times in normal edgelist circumstances
            sum = 0 
            #print "entry"
            for k in range(len(m1[0])):
                try:
                    sum += m1[i][k] * m2[k][j]
                except:
                    print("p len: " + str(len(m2)))
                    print("p[0] len: " + str(len(m2[0])))

#                    display_mtrx(m1)
#                    display_mtrx(m2)
#                    print("i: " + str(i))
#                    print("k: " + str(k))
#                    print("j: " + str(j))

            line.append(sum)
        m3.append(line)
    return m3
                       
def display_mtrx(matrix):
     for i in range(len(matrix[0])):
         s = ""
         for j in range(len(matrix)):
             s += str(matrix[j][i]) + " "
         print s

# GRAPHICS MATRIX STUFF

def add_point(matrix, x, y, z):
    matrix.append([x, y, z, 1.0])
    return matrix

def add_edge(matrix, x1, y1, z1, x2, y2, z2):
    matrix = add_point(matrix, x1, y1, z1)
    matrix = add_point(matrix, x2, y2, z2)
    return matrix

def add_polygon(matrix, p1, p2, p3):
    matrix = add_point(matrix, p1[0], p1[1], p1[2])
    matrix = add_point(matrix, p2[0], p2[1], p2[2])
    matrix = add_point(matrix, p3[0], p3[1], p3[2])
    return matrix

def get_coefficients(type, vals):
    #values will be p0, p1, m0, m1 for hermite and p0, p1, p2, p3 for bezier
    m = []
    m.append(vals)

    coefficients = []
    if type == "h":
        coefficients = mtrx_mult(m, hermite_mtrx())
    elif type == "b":
        coefficients = mtrx_mult(m, bezier_mtrx())

    return coefficients[0] # because it's a matrix and i want an array


'''
m1 = [[1, 6, 3],
      [2, 4, 7]]

m2 = [[1, 2],
      [3, 4],
      [5, 6]]

m3 = matrix_mult(m1, m2)
display_mtrx(m3)
'''
