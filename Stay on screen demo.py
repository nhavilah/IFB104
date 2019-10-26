#stay on screen demo

from turtle import*

#set up canvas and cursor
setup()
turtlesize(3)
shape('turtle')
color('green')
speed('fastest')
penup()
tracer(False)

#do this action repeatedly
for step in range(5000000):
    #decide whether to turn
    if xcor() > 250:
        left(180)
        color('red')
    if xcor() < -250:
        left(180)
        color('blue')
    #move turtle
    forward(10)
    update()

#exit
done()
