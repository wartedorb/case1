# Case-study №1
# Developers: Kondrashov M. (60%)
# Bikmetov E. (35%)
# Bychkov K. (25%)
# To do:
# #Kirill: 2 humans
# Max: Defs, main figure, rocket
# #Ed:Boat, Helicopter
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

# painting a main figure
tr.goto(100, 100)
triangle(180, 'red', 200)
# 1 triangle
square(70.71067811865475, 315)
# square
tr.up()
tr.goto(100, 0)
tr.down()
triangle(90, 'purple', 100)
# 2 triangle
tr.up()
tr.goto(101, 0)
tr.down()
triangle(225, 'cyan', 142.4213562373095)
# 3 triangle
tr.up()
tr.goto(-50, -50)
tr.down()
triangle(0, 'pink', 100)
# 4 triangle
tr.up()
tr.goto(-100, -100)
tr.down()
parallelogram(100, 69, 0)
# parallerogram
tr.up()
tr.goto(-100, 100)
tr.down()
# 5 triangle
triangle(270, 'yellow', 200)
# Main figure is done
#Painting a rocket
tr.up()
tr.goto(200, -140)
tr.down()
triangle(0, 'pink', 40) #1 triangle
tr.up()
tr.goto(200,-140)
tr.down()
triangle(315,'cyan', 56.5685424949238) #2 triangle
tr.up()
tr.goto(200, -140)
tr.down()
triangle(270,'yellow', 80) #3 triangle
tr.up()
tr.goto(240, -260)
tr.down()
triangle(90, 'red', 80) #4 triangle
tr.up()
tr.goto(200,-220 )
square(28.2842712474619, 225) #square
tr.up()
tr.goto(180,-240)
tr.down()
triangle(270, 'purple', 40.5) #5 triangle
tr.up()
tr.goto(240, -220)
tr.down()
parallelogram(40, 28.2842712474619, 270) #parallelogram
#rocket is done

# Helicopter
tr.speed(100)
tr.up()
tr.goto(-30,-140)
tr.down()
triangle(0, "cyan",60)
tr.up()
tr.goto(30,-139)
parallelogram(50,30,0)
tr.up()
tr.goto(30, -141)
triangle(270, "red", 100)
tr.up()
tr.goto(27,-241)
triangle(90, "yellow", 100)
tr.up()
tr.goto(-51,-218)
triangle(0,"purple", 50)
tr.up()
tr.goto(-30,-192)
triangle(180, "pink", 50)
tr.up()
tr.goto(-90, -202)
square(45, 45)
# Boat
tr.up()
tr.goto(-172,-140)
triangle(135,'purple',40)
tr.up()
tr.goto(-200,-140)
triangle(270,'red',100)
tr.up()
tr.goto(-198,-240)
triangle(0,'pink',50)
tr.up()
tr.goto(-148, -190)
square(34, 225)
tr.up()
tr.goto(-202,-165)
triangle(225,'yellow',85)
tr.up()
tr.goto(-150,-242)
triangle(180,"cyan",90)
tr.up()
tr.goto(-200,-287)
parallelogram(62,35,135)
# Painting a human 1
tr.up()
tr.goto(-160 - 20, 35 * 1.4)
tr.down()
square(28.2842712474619, 45)
tr.up()
tr.goto(-170 - 20, -8 * 1.33)
tr.down()
triangle(45, 'red', 80)
tr.up()
tr.goto(-170 - 20, 35 * 1.4)
tr.down()
parallelogram(40, 28.2842712474619, 225)
tr.up()
tr.goto(-150 + 20 * 0.33 - 20, 12 * 1.33)
tr.down()
triangle(225, 'yellow', 80)
tr.up()
tr.goto(-150 + 20 * 0.33 - 20, -14 * 1.4)
tr.down()
triangle(270, 'cyan', 56.5685424949238)
tr.up()
tr.goto(-150 + 20 * 0.33 - 20, -64 * 1.5)
tr.down()
triangle(90, 'purple', 40)
tr.up()
tr.goto(-200 - 50 * 0.33 - 20, -40 * 1.43)
tr.down()
triangle(45, 'pink', 40)
# Human 1 is done

# Painting a human 2
tr.up()
tr.goto(160 + 20, 35 * 1.4)
tr.down()
square(28.2842712474619, 45)
tr.up()
tr.goto(160 + 20, -7 * 1.33)
tr.down()
triangle(45, 'yellow', 80)
tr.up()
tr.goto(162 + 20, -5)
tr.down()
parallelogram(40, 28.2842712474619, 225)
tr.up()
tr.goto(118.5 - 41.5 * 0.33 + 20, 35 * 1.33)
tr.down()
triangle(315, 'red', 80)
tr.up()
tr.goto(201 + 20, -48)
tr.down()
triangle(135, 'cyan', 56.5685424949238)
tr.up()
tr.goto(183 + 20, -47.5)
tr.down()
triangle(315, 'purple', 40)
tr.up()
tr.goto(147.7 + 20, -47.3)
tr.down()
triangle(45 + 180, 'pink', 40)
# Human 2 is done
tr.hideturtle()

tr.done()
