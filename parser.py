from piecewise import *
from transform import *
from display import *
from matrix import *
from draw import *

from time import sleep
from math import pi


def parse_file(fname, points, transform, screen, color):

    stack = [identity_mtrx()]
    tpolys = []
    f = open(fname, 'r')
    lines = f.readlines()
    i = 0
    while i < len(lines):
        cmd = lines[i].strip()
        
        #print(cmd)
        #display_mtrx(stack[-1])
#        try:
        if cmd == "line":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])
            i += 2
        elif cmd == "ident":
            transform = identity_mtrx()
            i += 1
        elif cmd == "scale":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            stack[-1] = scale(stack[-1], args[0], args[1], args[2])
            i += 2
        elif cmd == "move":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            stack[-1] = translate(stack[-1], args[0], args[1], args[2])
            i += 2
        elif cmd == "rotate":
            args = lines[i+1].strip().split()
            theta = (float(args[1])/180) * pi
            if args[0] == "x":
                stack[-1] = rotateX(stack[-1], theta)
            elif args[0] == "y":
                stack[-1] = rotateY(stack[-1], theta)
            elif args[0] == "z":
                stack[-1] = rotateZ(stack[-1], theta)
            else:
                raise Exception("not an axis, try again")
            i += 2
        elif cmd == "circle":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_circle(points, args[0], args[1], args[2], args[3])
            i += 2
        elif cmd == "hermite":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_curve(points, "h", args)
            i += 2
        elif cmd == "bezier":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_curve(points, "b", args)
            i += 2
        elif cmd == "box":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_box(tpolys, args[0], args[1], args[2], args[3], args[4], args[5])
            tpolys = mtrx_mult(tpolys, stack[-1])
            
            draw_polygons(screen, tpolys, color)
            tpolys = []
            i += 2
        elif cmd == "sphere":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_sphere(tpolys, args[0], args[1], args[2], args[3])
            tpolys = mtrx_mult(tpolys, stack[-1])
            draw_polygons(screen, tpolys, color)
            tpolys = []
            i += 2
        elif cmd == "torus":
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_torus(tpolys, args[0], args[1], args[2], args[3], args[4])
            tpolys = mtrx_mult(tpolys, stack[-1])
            draw_polygons(screen, tpolys, color)
            tpolys = []
            i += 2
        elif cmd == "clear":
            points = []
            transform = identity_mtrx()
            i += 1
        elif cmd == "push":
            #print("push")
            stack.append([col[:] for col in stack[-1]])
            i += 1
        elif cmd == "pop":
            stack.pop()
            i += 1
        elif cmd == "apply":
            display_mtrx(transform)
            points = mtrx_mult(points, transform)
            i += 1
        elif cmd == "display":
            sleep(1)
            draw_polygons(screen, points, color)
            display(screen)
            i += 1
        elif cmd == "save":
            arg = lines[i+1].strip()
            save_extension(screen, arg)
            i += 2
        elif cmd == "quit":
            return
        elif cmd[0] == "#":
            i += 1
        else:
            print("INVALID COMMAND:" + cmd)
            i += 1
#            raise Exception("invalid command" + cmd)
#        except:
#            print "invalid file to parse. please edit and try again"
