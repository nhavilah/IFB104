#gold star

from turtle import * 
#create a canvas
setup()
title('Gold star')
bgcolor('black')

#set up the pen
color('red')
width(10)
pendown()

for line in range(5):
    forward(300)
    right(144)


#shutdown
hideturtle()
done()
