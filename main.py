'''
from display import *
from draw import *
from matrix import *
import random

print "\ntesting identity matrix:"
m1 = identity_mtrx()
display_mtrx(m1)

print "\ntesting scalar multiplication:"
m2 = scalar_mult(m1, 5)
display_mtrx(m2)

print "\ntesting add edge:"
m3 = []
add_edge(m3, 100, 100, 1, 200, 200, 1)
add_edge(m3, 200, 200, 1, 300, 200, 1)
add_edge(m3, 300, 200, 1, 400, 300, 1)
display_mtrx(m3)

print "\ntesting matrix mult:"
tmtrx = [[1, 2, 3, 4],
         [2, 1, 2, 3],
         [3, 2, 1, 2],
         [4, 3, 2, 1]]

m4 = mtrx_mult(m3, tmtrx)
display_mtrx(m4)


screen = new_screen()
color = [ 0, 255, 0 ]
draw_lines(screen, m3, color)


for i in range(100):
    (screen, 250, 250, int(random.random() * 500), int(random.random() * 500), color)

draw_line(screen, 250, 250, 100, 0, color)
draw_line(screen, 120, 0, 250, 250, color)
color = [ 255, 0, 255 ]
draw_line(screen, 250, 250, 0, 0, color)
draw_line(screen, 250, 250, 0, 250, color)
draw_line(screen, 250, 250, 0, 500, color)
draw_line(screen, 250, 250, 250, 500, color)
draw_line(screen, 250, 250, 500, 500, color)
draw_line(screen, 250, 250, 500, 250, color)
draw_line(screen, 250, 250, 500, 0, color)
draw_line(screen, 250, 250, 250, 0, color)

display(screen)
save_extension(screen, 'img.png')
'''

from parser import *
from display import *
from matrix import *
from script import *
#points = [[0.0, 0.0, 0.0, 1.0], [1.0, 1.0, 1.0, 1.0]]
points = []
transform = identity_mtrx()
screen = new_screen()
color = [0, 255, 0]

run("script.mdl")
