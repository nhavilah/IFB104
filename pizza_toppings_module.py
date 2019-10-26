#pizza toppings functions
#need to import turtle functions in this module too
from turtle import*
from random import*


#define a function that draws one piece of cheese
def cheese(angle,how_far):
    color('gold')
    shape('circle')
    turtlesize(uniform(0.2,1.0),uniform(0.2,1.0))
    home()
    setheading(angle)
    forward(how_far)
    stamp()

#define a function to put anchovies on pizza
def fishies(edible_radius,num_slices=6,how_many=100000):
    color('indigo')
    shape('arrow')
    turtlesize(0.5,2)
    for anchovy in range(how_many):
        home()
        setheading(randint(0,num_slices*60))
        forward(randint(edible_radius // 5,edible_radius))
        setheading(randint(0,359))
        stamp()
