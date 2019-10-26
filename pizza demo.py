##fat pizza drawing
#using pre defined functions and creating new modules to create a pizza
from turtle import*
from random import randint,uniform
from pizza_toppings_module import*
#set up canvas
setup(500,500)
title('fat pizza')
tablecloth = 'sea green'
bgcolor(tablecloth)
penup()
speed('fastest')

#define some useful constants
diameter = 300
crust = 50
radius=diameter//2

#draw pizza base
pencolor('tan')
dot(diameter)

#draw sauce
pencolor('dark red')
dot(diameter-crust)

#add toppings


#do cheese first
tracer(False) #dont dra it because it takes too long
for cheeses in range(1000):
   cheese((randint(0,359)),(randint(radius//7,radius-crust)))

#draw fishies
fishies(radius-crust)

#cut the pizza
tracer(True)#allows the cuts to be made
penup()
home()
pencolor(tablecloth)
shape('classic')
width(3)
pendown()
for cut in range(6):
    forward(radius)
    goto(0,0)
    left(60)

#exit gracefully
hideturtle()
done()
