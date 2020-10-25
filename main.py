import turtle as tr
import math
    tr.setup(1200,700)
    tr.speed(1000)
    def triangle(a, c,s):
    tr.color(c)
    tr.begin_fill()
    tr.left(a)
    tr.forward(s)
    tr.left(135)
    s2 = (math.sqrt(s**2/2)) #small side of a triangle
    tr.forward(s2)
    tr.left(90)
    tr.forward(s2)
    tr.left(135)
    tr.right(a)
    tr.end_fill()
    tr.color('white')
    tr.width(1.5)
    tr.left(a)
    tr.forward(s)
    tr.left(135)
    tr.forward(s2)
    tr.left(90)
    tr.forward(s2)
    tr.left(135)
    tr.width(1)
    tr.right(a)
    tr.up()
    tr.goto(0,0)
    tr.down()
    tr.color('black')
pass
'''
Paints mainly used colored triangle, where a is angle of its
rotation, c is its colour, s is the bigest side of triangle
'''
def square(a,c):
    tr.color('orange')
    tr.begin_fill()
    tr.left(c)
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.left(90)
    tr.right(c)
    tr.end_fill()
    tr.color('white')
    tr.width(1.5)
    tr.left(c)
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.left(90)
    tr.right(c)
    tr.width(1)
    tr.up()
    tr.goto(0, 0)
    tr.down()
    tr.color('black')
pass
'''
Paints orange square, where c is angle of its rotation, and a is
its side
'''
def parallelogram(b1,b2,a):

    tr.color('green')
    tr.left(a)
    tr.begin_fill()
    tr.forward(b1) #big side
    tr.left(45)
    tr.forward(b2) #small side
    tr.left(135)
    tr.forward(b1)
    tr.left(45)
    tr.forward(b2)
    tr.left(135)
    tr.end_fill()
    tr.color('white')
    tr.width(1.5)
    tr.forward(b1)
    tr.left(45)
    tr.forward(b2)
    tr.left(135)
    tr.forward(b1)
    tr.left(45)
    tr.forward(b2)
    tr.left(135)
    tr.right(a)
    tr.up()
    tr.goto(0, 0)
    tr.down()
    tr.color('black')
pass
'''
Paints parallelogram, where b1 is its big side, b2 is its small side,
a is the angle of its rotation
'''
