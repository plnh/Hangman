# # Turtle Graphics Baisc

# import turtle
# import random

# ha = turtle.Turtle()
# colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange','black']

# #set color
# ha.color('red','blue') # red is outline color and blue is fill color

# #set width
# ha.width(5)

# #Fill shape with color
# ha.begin_fill()
# ha.circle(50) # make a circle with a R = 50
# ha.end_fill()

# ha.penup()
# ha.forward(150)
# ha.pendown


# ha.color('yellow', 'black')
# ha.begin_fill()
# for x in range(4):
#     ha.fd(100)
#     ha.rt(90)
# ha.end_fill()

# for x in range(5):
    
#     ha.color(colors[random.randrange(0,len(colors))],colors[random.randrange(0,len(colors))])
#     rand1 = random.randrange(-300,300)
#     rand2 = random.randrange(-200,200)
#     ha.penup()
#     ha.setpos(rand1,rand2)
#     ha.pendown()
#     ha.begin_fill()
#     ha.circle(random.randrange(0,80))
#     ha.end_fill()
    
    
# # Key Presses

# import turtle
# import random
# from turtle import *

# ha = turtle.Turtle()
# ha.speed(0)
# ha.width(5)

# colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange','black']

# #function to move turtle
# def up():
#     ha.setheading(90) #point uppward
#     ha.forward(100)
    
# def down():
#     ha.setheading(270) #point downward
#     ha.forward(100)
    
# def left():
#     ha.setheading(180) 
#     ha.forward(100)
    
# def right():
#     ha.setheading(0) 
#     ha.forward(100)
    
# def clickleft(x,y): #switch colors
#     ha.color(random.choice(colors))
    
# def clickright(x,y):   #stamp down the arrow
#     ha.stamp()
    
# #events : anythings the user does

# turtle.listen() # turle listen to the event

# # 1 : left button 2 : middle and 3 : right
# #turtle.onclick(clickleft, 1)  # click on the turtle
# turtle.onscreenclick(clickleft, 1) #click on screen
# turtle.onscreenclick(clickright, 3)

# turtle.onkey(up, 'Up')
# turtle.onkey(down, 'Down')
# turtle.onkey(left, 'Left') # turtle.onkey(function defined above, Event/Input)
# turtle.onkey(right, 'Right')


# turtle.mainloop() # continue look for the event above until the program is closed


# Drawing with mouse

import turtle
from turtle import Turtle, Screen

screen = Screen()
ha = Turtle('turtle')
ha.speed(-1)

def dragging(x,y):
    ha.ondrag(None)
    ha.setheading(ha.towards(x,y)) #change direction to  x,y :the position of the mouse
    ha.goto(x,y) # move the arrow to the mouse
    ha.ondrag(dragging) # continue to call the dragging fun if keep dragging
    
def clickright(x,y): # clear the screen
    ha.clear()
    
  
        
def main():
    turtle.listen()
    
    turtle.onscreenclick(clickright, 3)
      
    ha.ondrag(dragging)
    screen.mainloop()

    
main()
    
























