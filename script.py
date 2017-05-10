import mdl
from piecewise import *
from transform import *
from display import *
from matrix import *
from draw import *

from time import sleep
from math import pi

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = identity_mtrx()

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    tmp = []
    step = 0.1
    for command in commands:
        cmd = command[0]
        args = []
        if len(command) > 1:
            args = command[1:]
        
        if cmd == "line":
            tmp = add_edge(tmp, float(args[0]), float(args[1]), float(args[2]), float(args[3]), float(args[4]), float(args[5]))
            tmp = mtrx_mult(tmp, stack[-1])
            draw_lines(tmp)
            tmp = []

        elif cmd == "scale":
            stack[-1] = scale(stack[-1], float(args[0]), float(args[1]), float(args[2]))
            
        elif cmd == "move":
            stack[-1] = translate(stack[-1], float(args[0]), float(args[1]), float(args[2]))

        elif cmd == "rotate":
            theta = (float(args[1])/180) * pi
            if args[0] == "x":
                stack[-1] = rotateX(stack[-1], theta)
            elif args[0] == "y":
                stack[-1] = rotateY(stack[-1], theta)
            elif args[0] == "z":
                stack[-1] = rotateZ(stack[-1], theta)
            else:
                raise Exception("not an axis, try again")

        elif cmd == "box":
            tmp = add_box(tmp, float(args[0]), float(args[1]), float(args[2]), float(args[3]), float(args[4]), float(args[5]))
            tmp = mtrx_mult(tmp, stack[-1])            
            draw_polygons(screen, tmp, color)
            tmp = []

        elif cmd == "sphere":
            tmp = add_sphere(tmp, float(args[0]), float(args[1]), float(args[2]), float(args[3]))
            tmp = mtrx_mult(tmp, stack[-1])
            draw_polygons(screen, tmp, color)
            tmp = []

        elif cmd == "torus":
            tmp = add_torus(tmp, float(args[0]), float(args[1]), float(args[2]), float(args[3]), float(args[4]))
            tmp = mtrx_mult(tmp, stack[-1])
            draw_polygons(screen, tmp, color)
            tmp = []

        elif cmd == "push":
            stack.append([col[:] for col in stack[-1]])
            
        elif cmd == "pop":
            stack.pop()
            
        elif cmd == "display":
            sleep(1)
            display(screen)
            
        elif cmd == "save":
            save_extension(screen, args[0])
            
        elif cmd == "quit":
            return
        elif cmd[0] == "#":
            i += 1
        else:
            print("INVALID COMMAND:" + cmd)
            i += 1
