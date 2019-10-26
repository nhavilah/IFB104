
#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task I agree that it represents my own work.
#  I am aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#  Student no:      n10469231
#  Student name:    Nicholas Havilah
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#




from turtle import *

#set up the turtule canvas
setup()
title('Concentric Squares')

# define some basic variables for the width of the square and pens
#these variables are the only part of the code you need to modify to get different sized squares
square_width = [200,145,85,0]#the last variable in this list is a placeholder for the calculations-DO NOT DELETE IT!!-it needs to be in the calculations but the value makes no difference to the result
pen_thickness= [5,6,5]
colours = ['red','blue','green']

#make the for loop to create the concentric squares
for x in range(3):
    penup()
    #define the colour of the box
    fillcolor(colours[x])
    begin_fill()
    #draw the lines of the box
    for box in range(4):
        width(pen_thickness[x])
        pendown()
        forward(square_width[x])
        left(90)
    end_fill()    
    #reset the cursor position
    #the reset needs to put the square in a place where the smaller one can be placed
    penup()
    #reset the cursor then move to the new position to draw the smaller box
    home()
    setheading(0)
    if x==1:#this if statement checks what x value we are up to and then will use different variables from the square_width list to calculate
        forward((square_width[x-1]-(square_width[x+1]))/2)
        left(90)
        forward((square_width[x-1]-(square_width[x+1]))/2)
        right(90)
    #this elif statement calculates the position the cursor needs to be at to draw the second square
    elif x != 1:
        forward((square_width[x]-(square_width[x+1]))/2)
        left(90)
        forward((square_width[x]-(square_width[x+1]))/2)
        right(90)
        

#exit gracefully
hideturtle()
done()


