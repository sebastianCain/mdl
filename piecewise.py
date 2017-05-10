from math import sin, cos, pi
from matrix import *
from draw import *

def circx(x, t, r):
    return r * cos(2 * pi * t) + x

def circy(y, t, r):
    return r * sin(2 * pi * t) + y

def add_circle(matrix, x, y, z, r):
    return draw_parametric(matrix, x, y, z, r, circx, circy, 0.01)

def cubicx(x, t, c):
    #xc is x coefficients
    xc = c[0]
    return (xc[0] * (t ** 3)) + (xc[1] * (t ** 2)) + (xc[2] * t) + xc[3] 

def cubicy(y, t, c):
    #yc is y coefficients
    yc = c[1]
    return (yc[0] * (t ** 3)) + (yc[1] * (t ** 2)) + (yc[2] * t) + yc[3]

def add_curve(matrix, type, vals):

    xdata = vals[::2]
    ydata = vals[1::2]
    
    xc = get_coefficients(type, xdata)
    yc = get_coefficients(type, ydata)

    coeffs = [xc, yc]

    return draw_parametric(matrix, vals[0], vals[1], 0, coeffs, cubicx, cubicy, 0.01) 


def generate_sphere(cx, cy, cz, r):
    pts = []

    qual = 10
    step = 1/float(qual)

    rot = 0.0
    while rot < 1.01:        
        circ = 0.0
        while circ < 1.01:
            point = []
            point.append(r * cos(2 * pi * circ) + cx)
            point.append(r * sin(2 * pi * circ) * cos(2 * pi * rot) + cy)
            point.append(r * sin(2 * pi * circ) * sin(2 * pi * rot) + cz)
            point.append(1)

            pts.append(point)

            circ += step
        rot += step
    print("pts len: " + str(len(pts)))
    #points now has all the significant points
    plen = len(pts)
    q1 = qual + 1
    polys = []
    for i in range(0, q1):
        polys = add_polygon(polys, pts[i*q1], pts[(i*q1)+1], pts[(((i+1)*q1)+1) % plen]) 
        for j in range(1, q1-1):
            polys = add_polygon(polys, pts[(i*q1)+j], pts[(i*q1)+j+1], pts[(((i+1)*q1)+j) % plen])
            polys = add_polygon(polys, pts[(i*q1)+j+1], pts[(((i+1)*q1)+j+1) % plen], pts[(((i+1)*q1)+j) % plen])
        polys = add_polygon(polys, pts[(i*q1)+q1-1], pts[(((i+1)*q1)+q1-2) % plen], pts[(i*q1)+q1-2]) 
        
    return polys

def add_sphere(matrix, x, y, z, r):
    pts = generate_sphere(x, y, z, r)
    i = 0
    while i < len(pts):
        matrix = add_polygon(matrix, pts[i], pts[i+1], pts[i+2])
        i += 3
    return matrix

def generate_torus(cx, cy, cz, r, R):
    pts = []

    qual1 = 40
    qual2 = 10
    step1 = 1/float(qual1)
    step2 = 1/float(qual2)

    rot = 0.01
    while rot < 1.001:
        circ = 0.01
        while circ < 1.001:
            point = []
            point.append(cos(2 * pi * rot) * (r * cos(2 * pi * circ) + R) + cx)
            point.append(r * sin(2 * pi * circ) + cy)
            point.append(-(sin(2 * pi * rot)) * (r * cos(2 * pi * circ) + R) + cz)
            point.append(1)

            pts.append(point)

            circ += step2
        rot += step1

    #points now complete
    plen = len(pts)
    print(plen)
    q1 = qual1
    q2 = qual2
    polys = []
    for i in range(0, q1):
        for j in range(0, q2):
            print("i: " + str(i) + " j: " + str(j))
            polys = add_polygon(polys, pts[(i*q2)+j], pts[(i*q2)+((j+1)%q2)], pts[(((i+1)*q2)+j) % plen])
            polys = add_polygon(polys, pts[(i*q2)+((j+1)%q2)], pts[(((i+1)*q2)+((j+1)%q2)) % plen], pts[(((i+1)*q2)+j) % plen])
    return polys

def add_torus(matrix, x, y, z, r, R):
    pts = generate_torus(x, y, z, r, R)
    i = 0
    while i < len(pts):
        matrix = add_polygon(matrix, pts[i], pts[i+1], pts[i+2])
        i += 3
    return matrix

def generate_box(cx, cy, cz, w, h, d):
    pts = [[cx, cy, cz, 1],
           [cx+w, cy, cz, 1],
           [cx, cy-h, cz, 1],
           [cx, cy, cz-d, 1],
           [cx+w, cy-h, cz, 1],
           [cx, cy-h, cz-d, 1],
           [cx+w, cy, cz-d, 1],
           [cx+w, cy-h, cz-d, 1]]

    polys = [pts[0], pts[2], pts[4],
             pts[0], pts[4], pts[1],
             pts[1], pts[4], pts[7],
             pts[1], pts[7], pts[6],
             pts[6], pts[7], pts[5],
             pts[6], pts[5], pts[3],
             pts[3], pts[5], pts[2],
             pts[3], pts[2], pts[0],
             pts[3], pts[0], pts[1],
             pts[3], pts[1], pts[6],
             pts[2], pts[5], pts[7],
             pts[2], pts[7], pts[4]]

    return polys

def add_box(matrix, x, y, z, w, h, d):
    pts = generate_box(x, y, z, w, h, d)
    print(str(len(pts)))
    i = 0
    while i < len(pts):
        matrix = add_polygon(matrix, pts[i], pts[i+1], pts[i+2])
        i += 3
    return matrix
