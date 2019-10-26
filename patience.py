
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10469231
#    Student name: NICHOLAS HAVILAH
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
# PATIENCE
#
# This assignment tests your skills at processing data stored in
# lists, creating reusable code and following instructions to display
# a complex visual image.  The incomplete Python program below is
# missing a crucial function, "deal_cards".  You are required to
# complete this function so that when the program is run it draws a
# game of Patience (also called Solitaire in the US), consisting of
# multiple stacks of cards in four suits.  See the instruction sheet
# accompanying this file for full details.
#
# Note that this assignment is in two parts, the second of which
# will be released only just before the final deadline.  This
# template file will be used for both parts and you will submit
# your final solution as a single Python 3 file, whether or not you
# complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be installed separately, because the markers
# will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

# Constants defining the size of the card table
table_width = 1100 # width of the card table in pixels
table_height = 800 # height (actually depth) of the card table in pixels
canvas_border = 30 # border between playing area and window's edge in pixels
half_width = table_width // 2 # maximum x coordinate on table in either direction
half_height = table_height // 2 # maximum y coordinate on table in either direction

# Work out how wide some text is (in pixels)
def calculate_text_width(string, text_font = None):
    penup()
    home()
    write(string, align = 'left', move = True, font = text_font)
    text_width = xcor()
    undo() # write
    undo() # goto
    undo() # penup
    return text_width

# Constants used for drawing the coordinate axes
axis_font = ('Consolas', 10, 'normal') # font for drawing the axes
font_height = 14 # interline separation for text
tic_sep = 50 # gradations for the x and y scales shown on the screen
tics_width = calculate_text_width("-mmm -", axis_font) # width of y axis labels

# Constants defining the stacks of cards
stack_base = half_height - 25 # starting y coordinate for the stacks
num_stacks = 6 # how many locations there are for the stacks
stack_width = table_width / (num_stacks + 1) # max width of stacks
stack_gap = (table_width - num_stacks * stack_width) // (num_stacks + 1) # inter-stack gap
max_cards = 10 # maximum number of cards per stack

# Define the starting locations of each stack
stack_locations = [["Stack " + str(loc + 1),
                    [int(-half_width + (loc + 1) * stack_gap + loc * stack_width + stack_width / 2),
                     stack_base]] 
                    for loc in range(num_stacks)]


# Same as Turtle's write command, but writes upside down
def write_upside_down(string, **named_params):
    named_params['angle'] = 180
    tk_canvas = getscreen().cv
    tk_canvas.create_text(xcor(), -ycor(), named_params, text = string)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# create the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the coordinate axes displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_axes = False):

    # Set up the drawing canvas
    setup(table_width + tics_width + canvas_border * 2,
          table_height + font_height + canvas_border * 2)

    # Draw as fast as possible
    tracer(False)

    # Make the background felt green and the pen a lighter colour
    bgcolor('green')
    pencolor('light green')

    # Lift the pen while drawing the axes
    penup()

    # Optionally draw x coordinates along the bottom of the table
    if show_axes:
        for x_coord in range(-half_width + tic_sep, half_width, tic_sep):
            goto(x_coord, -half_height - font_height)
            write('| ' + str(x_coord), align = 'left', font = axis_font)

    # Optionally draw y coordinates to the left of the table
    if show_axes:
        max_tic = int(stack_base / tic_sep) * tic_sep
        for y_coord in range(-max_tic, max_tic + tic_sep, tic_sep):
            goto(-half_width, y_coord - font_height / 2)
            write(str(y_coord).rjust(4) + ' -', font = axis_font, align = 'right')

    # Optionally mark each of the starting points for the stacks
    if show_axes:
        for name, location in stack_locations:
            # Draw the central dot
            goto(location)
            color('light green')
            dot(7)
            # Draw the horizontal line
            pensize(2)
            goto(location[0] - (stack_width // 2), location[1])
            setheading(0)
            pendown()
            forward(stack_width)
            penup()
            goto(location[0] -  (stack_width // 2), location[1] + 4)
            # Write the coordinate
            write(name + ': ' + str(location), font = axis_font)

    #Draw a border around the entire table
    penup()
    pensize(3)
    goto(-half_width, half_height) # top left
    pendown()
    goto(half_width, half_height) # top
    goto(half_width, -half_height) # right
    goto(-half_width, -half_height) # bottom
    goto(-half_width, half_height) # left

    # Reset everything, ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any partial drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the deal_cards function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_game function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_game function.
#

# Each of these fixed games draws just one card
fixed_game_0 = [['Stack 1', 'Suit A', 1, 0]]
fixed_game_1 = [['Stack 2', 'Suit B', 1, 0]]
fixed_game_2 = [['Stack 3', 'Suit C', 1, 0]]
fixed_game_3 = [['Stack 4', 'Suit D', 1, 0]]

# Each of these fixed games draws several copies of just one card
fixed_game_4 = [['Stack 2', 'Suit A', 4, 0]]
fixed_game_5 = [['Stack 3', 'Suit B', 3, 0]]
fixed_game_6 = [['Stack 4', 'Suit C', 2, 0]]
fixed_game_7 = [['Stack 5', 'Suit D', 5, 0]]

# This fixed game draws each of the four cards once
fixed_game_8 = [['Stack 1', 'Suit A', 1, 0],
                ['Stack 2', 'Suit B', 1, 0],
                ['Stack 3', 'Suit C', 1, 0],
                ['Stack 4', 'Suit D', 1, 0]]

# These fixed games each contain a non-zero "extra" value
fixed_game_9 = [['Stack 3', 'Suit D', 4, 4]]
fixed_game_10 = [['Stack 4', 'Suit C', 3, 2]]
fixed_game_11 = [['Stack 5', 'Suit B', 2, 1]]
fixed_game_12 = [['Stack 6', 'Suit A', 5, 5]]

# These fixed games describe some "typical" layouts with multiple
# cards and suits. You can create more such data sets yourself
# by calling function random_game in the shell window

fixed_game_13 = \
 [['Stack 6', 'Suit D', 9, 6],
  ['Stack 4', 'Suit B', 5, 0],
  ['Stack 5', 'Suit B', 1, 1],
  ['Stack 2', 'Suit C', 4, 0]]
 
fixed_game_14 = \
 [['Stack 1', 'Suit C', 1, 0],
  ['Stack 5', 'Suit D', 2, 1],
  ['Stack 3', 'Suit A', 2, 0],
  ['Stack 2', 'Suit A', 8, 5],
  ['Stack 6', 'Suit C', 10, 0]]

fixed_game_15 = \
 [['Stack 3', 'Suit D', 0, 0],
  ['Stack 6', 'Suit B', 2, 0],
  ['Stack 2', 'Suit D', 6, 0],
  ['Stack 1', 'Suit C', 1, 0],
  ['Stack 4', 'Suit B', 1, 1],
  ['Stack 5', 'Suit A', 3, 0]]

fixed_game_16 = \
 [['Stack 6', 'Suit C', 8, 0],
  ['Stack 2', 'Suit C', 4, 4],
  ['Stack 5', 'Suit A', 9, 3],
  ['Stack 4', 'Suit C', 0, 0],
  ['Stack 1', 'Suit A', 5, 0],
  ['Stack 3', 'Suit B', 5, 0]]

fixed_game_17 = \
 [['Stack 4', 'Suit A', 6, 0],
  ['Stack 6', 'Suit C', 1, 1],
  ['Stack 5', 'Suit C', 4, 0],
  ['Stack 1', 'Suit D', 10, 0],
  ['Stack 3', 'Suit B', 9, 0],
  ['Stack 2', 'Suit D', 2, 2]]
 
# The "full_game" dataset describes a random game
# containing the maximum number of cards
stacks = ['Stack ' + str(stack_num+1) for stack_num in range(num_stacks)]
shuffle(stacks)
suits = ['Suit ' + chr(ord('A')+suit_num) for suit_num in range(4)]
shuffle(suits)
full_game = [[stacks[stack], suits[stack % 4], max_cards, randint(0, max_cards)]
             for stack in range(num_stacks)]

#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a game
# of Patience to be drawn.  Your program must work for any data set 
# returned by this function.  The results returned by calling this 
# function will be used as the argument to your deal_cards function 
# during marking. For convenience during code development and marking 
# this function also prints the game data to the shell window.
#
# Each of the data sets generated is a list specifying a set of
# card stacks to be drawn. Each specification consists of the
# following parts:
#
# a) Which stack is being described, from Stack 1 to num_stacks.
# b) The suit of cards in the stack, from 'A' to 'D'.
# c) The number of cards in the stack, from 0 to max_cards
# d) An "extra" value, from 0 to max_cards, whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#
# There will be up to num_stacks specifications, but sometimes fewer
# stacks will be described, so your code must work for any number
# of stack specifications.
#
def random_game(print_game = True):

    # Percent chance of the extra value being non-zero
    extra_probability = 20

    # Generate all the stack and suit names playable
    game_stacks = ['Stack ' + str(stack_num+1)
                   for stack_num in range(num_stacks)]
    game_suits = ['Suit ' + chr(ord('A')+suit_num)
                  for suit_num in range(4)]

    # Create a list of stack specifications
    game = []

    # Randomly order the stacks
    shuffle(game_stacks)

    # Create the individual stack specifications 
    for stack in game_stacks:
        # Choose the suit and number of cards
        suit = choice(game_suits)
        num_cards = randint(0, max_cards)
        # Choose the extra value
        if num_cards > 0 and randint(1, 100) <= extra_probability: 
            option = randint(1,num_cards)
        else:
            option = 0
        # Add the stack to the game, but if the number of cards
        # is zero we will usually choose to omit it entirely
        if num_cards != 0 or randint(1, 4) == 4:
            game.append([stack, suit, num_cards, option])
        
    # Optionally print the result to the shell window
    if print_game:
        print('\nCards to draw ' +
              '(stack, suit, no. cards, option):\n\n',
              str(game).replace('],', '],\n '))
    
    # Return the result to the student's deal_cards function
    return game

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "deal_cards" function.
#
#define a function that puts the cards into a stack

def suit_a_draw():
    #draw the castle
    penup()
    setheading(0)
    forward(105)
    left(90)
    pendown()
    fillcolor('gray')
    begin_fill()
    setheading(0)
    forward(105)
    left(100)
    forward(75)
    setheading(0)
    forward(30)
    left(90)
    forward(45)
    left(90)
    forward(22.5)
    left(90)
    forward(15)
    right(90)
    forward(15)
    right(90)
    forward(15)
    left(90)
    forward(22.5)
    left(90)
    forward(15)
    right(90)
    forward(15)
    right(90)
    forward(15)
    left(90)
    forward(22.5)
    left(90)
    forward(15)
    right(90)
    forward(15)
    right(90)
    forward(15)
    left(90)
    forward(22.5)
    left(90)
    forward(45)
    left(90)
    forward(30)
    right(102)
    forward(75)
    end_fill()
    fillcolor('black')
    begin_fill()
    setheading(0)
    penup()
    forward(37.5)
    left(90)
    pendown()
    forward(15)
    setheading(90)
    circle(-15,extent=180)
    setheading(270)
    forward(15)
    end_fill()
    penup()
    setheading(180)
    forward(15)
    setheading(90)
    forward(60)
    right(90)
    forward(15)
    setheading(0)
    forward(7.5)
    pendown()
    fillcolor('black')
    begin_fill()
    setheading(90)
    forward(7.5)
    setheading(90)
    circle(7.5,extent=180)
    setheading(270)
    forward(7.5)
    left(90)
    forward(15)
    end_fill()
    penup()
    setheading(180)
    forward(30)
    pendown()
    fillcolor('black')
    begin_fill()
    setheading(90)
    forward(7.5)
    setheading(90)
    circle(7.5,extent=180)
    setheading(270)
    forward(7.5)
    left(90)
    forward(15)
    end_fill()
    #reset the cursor position
    penup()
    right(180)
    forward(60)
    right(90)
    forward(58.5)

def suit_b_draw():
    #draw the flag
    fillcolor('brown')
    begin_fill()
    setheading(0)
    forward(7.5)
    left(90)
    forward(180)
    left(90)
    forward(7.5)
    left(90)
    forward(180)
    left(90)
    forward(7.5)
    end_fill()
    penup()
    goto(xcor()-7.5,ycor()+180)
    setheading(180)
    fillcolor('black')
    begin_fill()
    pendown()
    circle(60,extent=45)
    circle(-60,extent=45)
    setheading(270)
    forward(75)
    setheading(180)
    circle(-60,extent=-45)
    circle(60,extent=-45)
    end_fill()
    penup()
    setheading(180)
    forward(45)
    right(90)
    forward(15)
    setheading(200)
    width(0)
    fillcolor('yellow')
    begin_fill()
    pendown()
    forward(15)
    right(90)
    forward(15)
    right(90)
    forward(4.5)
    right(90)
    forward(4.5)
    left(90)
    forward(3)
    left(90)
    forward(4.5)
    right(90)
    forward(3)
    right(90)
    forward(4.5)
    left(90)
    forward(3)
    left(90)
    forward(4.5)
    right(90)
    forward(3)
    right(90)
    forward(4.5)
    left(90)
    forward(4.5)
    left(90)
    forward(4.5)
    right(90)
    forward(4.5)
    right(90)
    forward(15)
    right(90)
    forward(13.5)
    end_fill()
def suit_c_draw():
    #draw the shield
    penup()
    setheading(0)
    fillcolor('blue')
    begin_fill()
    forward(90)
    right(90)
    forward(60)
    circle(-45,extent=90)
    setheading(90)
    forward(105)
    end_fill()
    setheading(270)
    fillcolor('red')
    begin_fill()
    forward(105)
    setheading(180)
    circle(-45,extent=90)
    setheading(90)
    forward(60)
    end_fill()
    setheading(0)
    forward(30)
    right(90)
    forward(45)
    pendown()
    pencolor('yellow')
    width(9)
    fillcolor('yellow')
    begin_fill()
    circle(15)
    end_fill()
    penup()
    setheading(90)
    forward(15)
    right(90)
    forward(15)
    setheading(90)
    pendown()
    forward(21)
    right(180)
    forward(72)
    right(180)
    forward(36)
    left(90)
    forward(36)
    right(180)
    forward(72)
    right(180)
    forward(36)
    setheading(45)
    forward(36)
    right(180)
    forward(72)
    right(180)
    forward(36)
    setheading(135)
    forward(36)
    right(180)
    forward(72)
def suit_d_draw():
    #draw the suit of armour
    fillcolor('gray')
    begin_fill()
    setheading(90)
    circle(30,extent=180)
    left(10)
    forward(30)
    left(15)
    forward(20)
    setheading(0)
    forward(33)
    left(65)
    forward(20)
    left(15)
    forward(30)
    end_fill()
    setheading(180)
    penup()
    forward(10)
    fillcolor('black')
    begin_fill()
    pendown()
    forward(15)
    right(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(15)
    left(90)
    forward(7)
    left(90)
    forward(15)
    right(90)
    forward(30)
    left(45)
    forward(7)
    left(90)
    forward(7)
    setheading(90)
    forward(30)
    right(90)
    forward(15)
    left(90)
    forward(7)
    end_fill()
    penup()
    setheading(270)
    forward(50)
    left(90)
    fillcolor('gray')
    begin_fill()
    pendown()
    forward(10)
    circle(10,extent=135)
    right(180)
    forward(35)
    circle(-10,extent=90)
    forward(20)
    right(110)
    forward(30)
    right(10)
    forward(10)
    left(170)
    forward(40)
    right(90)
    forward(30)
    circle(-5,extent=90)
    setheading(90)
    circle(5,extent=-90)
    right(190)
    forward(30)
    right(80)
    forward(37)
    right(90)
    forward(20)
    end_fill()
    penup()
    left(180)
    forward(10)
    right(90)
    pendown()
    begin_fill()
    forward(10)
    left(70)
    forward(20)
    circle(15,extent=90)
    left(90)
    forward(30)
    left(185)
    forward(20)
    circle(10,extent=120)
    left(90)
    forward(20)
    right(30)
    forward(13)
    setheading(180)
    forward(20)
    left(30)
    forward(10)
    circle(5,extent=180)
    right(10)
    forward(25)
    end_fill()
    left(20)
    forward(20)
    setheading(180)
    forward(20)
def joker_suit_draw():
    #draw the dragon
    fillcolor('green')
    begin_fill()
    setheading(270)
    circle(75,extent=-45)
    setheading(110)
    circle(-60,extent=45)
    left(90)
    forward(20)
    setheading(30)
    circle(60,extent=-60)
    setheading(225)
    forward(15)
    setheading(300)
    circle(-60,extent=50)
    left(60)
    circle(-67.5,extent=45)
    setheading(310)
    forward(30)
    left(90)
    forward(30)
    end_fill()
    penup()
    setheading(85)
    forward(112.5)
    fillcolor('tan')
    begin_fill()
    right(45)
    forward(27)
    right(150)
    forward(27)
    right(110)
    forward(12)
    end_fill()
    penup()
    setheading(180)
    forward(64.5)
    setheading(140)
    begin_fill()
    forward(22.5)
    left(150)
    forward(24)
    left(115)
    forward(10.5)
    end_fill()
    penup()
    setheading(270)
    forward(45)
    left(90)
    forward(18)
    fillcolor('red')
    begin_fill()
    left(125)
    forward(10.5)
    left(220)
    circle(-5.25,extent=-180)
    left(135)
    forward(4.5)
    setheading(0)
    forward(7.5)
    end_fill()
    penup()
    setheading(270)
    forward(64.5)
    left(90)
    forward(4.5)
    pencolor('black')
    dot()
    setheading(0)
    penup()
    forward(19.5)
    right(90)
    forward(1.5)
    pendown()
    dot()
    pencolor('white')
    penup()
    setheading(90)
    forward(67.5)
    right(90)
    forward(7.5)
    begin_fill()
    setheading(55)
    forward(15)
    right(270)
    circle(7.5,extent=-180)
    end_fill()
    setheading(0)
def draw_square(what_suit,card_numbers):
    #start drawing the cards
    penup()
    #sets the background colour for all the suits(except for the joker, but that is defined inside its if statement further down)
    fillcolor('white')
    if what_suit == 'Suit A':
        #draw the outline for the card
        for sides in range(2):
                width(3)
                begin_fill()
                pendown()
                forward(150)
                right(90)
                forward(200)
                right(90)
                end_fill()
                penup()
        #draw the castle
        #move the cursor to a position that lets the castle be in the centre of the card
        penup()
        setheading(0)
        forward(-83)
        right(90)
        forward(150)
        current_x=xcor()
        current_y=ycor()
        setheading(0)
        suit_a_draw()
        setheading(0)
        penup()
        goto(current_x+83,current_y+150)
        #write the numbers on the card
        setheading(0)
        forward(15)
        right(90)
        forward(25)
        setheading(0)
        write(card_numbers)
        penup()
        current_x=xcor()
        current_y=ycor()
        goto(current_x-15,current_y+25)
        #move the cursor to the bottom right corner of the card
        setheading(0)
        forward(150)
        right(90)
        forward(200)
        setheading(180)
        forward(15)
        right(90)
        forward(25)
        write_upside_down(card_numbers)
        #return the cursor to the top left corner of the card
        setheading(0)
        current_x=xcor()
        current_y=ycor()
        penup()
        goto(current_x-135,current_y+175)
                
    if what_suit == 'Suit B':
        #draw the card outline
        for sides in range(2):
                width(3)
                begin_fill()
                pendown()
                forward(150)
                right(90)
                forward(200)
                right(90)
                end_fill()
                penup()
        #draw the flag on the card
        #move the cursor further into the card then write the number
        penup()
        setheading(0)
        forward(120)
        right(90)
        forward(190)
        current_x=xcor()
        current_y=ycor()
        setheading(0)
        suit_b_draw()
        setheading(0)
        penup()
        goto(current_x-120,current_y+190)
        #write the card number
        forward(15)
        right(90)
        forward(25)
        setheading(0)
        write(card_numbers)
        penup()
        #return the cursor to the top left corner of the card
        current_x=xcor()
        current_y=ycor()
        goto(current_x-15,current_y+25)
        #move the cursor to the bottom right corner to draw the upside down number
        setheading(0)
        forward(150)
        right(90)
        forward(200)
        setheading(180)
        forward(15)
        right(90)
        forward(25)
        write_upside_down(card_numbers)
        #return to the top left corner of the card
        setheading(0)
        current_x=xcor()
        current_y=ycor()
        penup()
        goto(current_x-135,current_y+175)
                
    if what_suit == 'Suit C':
        #draws the card outline and fills it in
        for sides in range(2):
                width(3)
                begin_fill()
                pendown()
                forward(150)
                right(90)
                forward(200)
                right(90)
                end_fill()
                penup()
        #draw the shield
        #moves the cursor into a position that allows the shield to be drawn in the centre of the card
        setheading(0)
        forward(30)
        right(90)
        forward(37.5)
        current_x=xcor()
        current_y=ycor()
        suit_c_draw()
        setheading(0)
        pencolor('black')
        penup()
        goto(current_x-30,current_y+37.5)
        #write the card number
        #moves the cursor further into the card to write the number
        forward(15)
        right(90)
        forward(25)
        setheading(0)
        write(card_numbers)
        #returns the card to the top left corner, then it moves the cursor to bottom right corner where the next number will be drawn upside down
        penup()
        current_x=xcor()
        current_y=ycor()
        goto(current_x-15,current_y+25)
        setheading(0)
        forward(150)
        right(90)
        forward(200)
        setheading(180)
        forward(15)
        right(90)
        forward(25)
        write_upside_down(card_numbers)
        #returns to the top left corner
        setheading(0)
        current_x=xcor()
        current_y=ycor()
        penup()
        goto(current_x-135,current_y+175)
    if what_suit == 'Suit D':   
        for sides in range(2):
                width(3)
                begin_fill()
                pendown()
                forward(150)
                right(90)
                forward(200)
                right(90)
                end_fill()
                penup()
        #draw the suit of armour
        #move the cursor to a psotion that allows the suit of armour o be drawn in the centre of the card
        setheading(0)
        forward(100)
        right(90)
        forward(60)
        current_x=xcor()
        current_y=ycor()
        suit_d_draw()
        setheading(0)
        penup()
        goto(current_x-100,current_y+60)
        #write the card number
        #move to the ideal position on the card
        forward(15)
        right(90)
        forward(25)
        setheading(0)
        write(card_numbers)
        penup()
        #return to the original position on the card in preparation for drawing the upside down number on the card
        current_x=xcor()
        current_y=ycor()
        goto(current_x-15,current_y+25)
        #move the cursor to the position in the bottom right hand corner of the card (where the upside down numbers will be written)
        setheading(0)
        forward(150)
        right(90)
        forward(200)
        setheading(180)
        forward(15)
        right(90)
        forward(25)
        write_upside_down(card_numbers)
        #return the cursor to the top left hand corner of the card in preparation to draw the next card in the stack
        setheading(0)
        current_x=xcor()
        current_y=ycor()
        penup()
        goto(current_x-135,current_y+175)
    if what_suit == 'joker':
        #draw the card border and use a black fill with a white border
        for sides in range(2):
                width(3)
                pencolor('white')
                fillcolor('black')
                begin_fill()
                pendown()
                forward(150)
                right(90)
                forward(200)
                right(90)
                end_fill()
                penup()
        #move the cursor into the centre of the screen-allows the dragon head to be drawn in the correct spot
        setheading(0)
        current_x=xcor()
        current_y=ycor()
        forward(100)
        right(90)
        forward(130)
        #begin drawing the dragon head for the joker suit
        joker_suit_draw()
        #reset the fill colour to black
        penup()
        goto(current_x,current_y)
        pencolor('black')
        
def stack_properties():
    #some constants to be used in the function that determine the number of stacks
    random_game()
    #use this variable to store the list that we will be working with for this instance-it will change and an index out of range error will appear
    current_game = random_game()  
    #length of the for loop
    how_many_stacks =  len(current_game)  
    stack_positions = stack_locations
    card_numbers=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    for positions in range(how_many_stacks):
        #this part of the for loop will determine how many stacks will have cards drawn in them
        current_stack = current_game[positions]
        #retrieves the suit from the list
        what_suit=current_game[positions][1]
        #grab the number in the string and then convert the number to an int
        #the stack number will always be at position so don't change this variable
        stack_number=int(current_game[positions][0][6])
        #compare the stack number to the reference list stack_locations
        reference_stack = stack_positions[stack_number-1]
        #retrieve the stack coordinates required(x and y)
        overall_reference_coordinates_x = reference_stack[1][0]
        overall_reference_coordinates_y = reference_stack[1][1]
        #move the cursor to the stack location - 50 to centre the card on the stack position
        goto(overall_reference_coordinates_x - 74,overall_reference_coordinates_y)
        #retrieves the joker position from the list
        joker_position_in_stack=current_game[positions][3]
        #randomises the starting number on the cards at the top of each stack
        current_card_number=randint(0,12)
        #takes the number from the list that corresponds to the position generated in the line above
        numbers_on_the_card=card_numbers[current_card_number]
        #this part of the for loop will determine how many cards go into each stack by creating a for loop to draw all of the necessary cards in each stack
        how_many_cards = current_stack[2]
        for cards in range(how_many_cards):
            #checks  if there is a non-zero number in the joker aspect of the list and if so it wil swap the suit to the joker suit 
            if joker_position_in_stack>0:
                if cards+1==joker_position_in_stack:
                    what_suit='joker'
                else:
                    #otherwise the suit remains the same
                    what_suit=current_stack[1]
            #have to use an if statement here to make sure that if there is only one card in a stack it won't double up
            draw_square(what_suit,numbers_on_the_card)
            penup()
            #retrieve current cursor position
            current_cursor_pos_x = xcor()
            current_cursor_pos_y =ycor()
            #returns to the original position of the cursor(before it was stored)
            goto(current_cursor_pos_x,current_cursor_pos_y - 50)
            pendown()
            #increments the next cards number by one
            current_card_number=current_card_number+1
            #resets the numbers to return to the start of the list
            if current_card_number==13:
                current_card_number=0
            numbers_on_the_card=card_numbers[current_card_number]        
        penup()
# Draw the card stacks as per the provided game specification
def deal_cards(rename_this_parameter):
    stack_properties()
#
#--------------------------------------------------------------------#
#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing the card game.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#
# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and stack locations
create_drawing_canvas()
# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')
# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)
# Give the drawing canvas a title
# ***** Replace this title with a description of your cards' theme
title("Medieval Solitare")
### Call the student's function to draw the game
### ***** While developing your program you can call the deal_cards
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_game()" as the
### ***** argument to the deal_cards function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_game function.
# deal_cards(fixed_game_0) # <-- used for code development only, not marking
# deal_cards(full_game) # <-- used for code development only, not marking
deal_cards(random_game()) # <-- used for assessment
# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas(True)
#
#--------------------------------------------------------------------#
