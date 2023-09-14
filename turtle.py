import turtle
pen = turtle.Turtle()

## Heart
 # Defining a method to draw curve
def curve():
    for i in range(200):
  
        # Defining step by step curve motion
        pen.right(1)
        pen.forward(1)
  
# Defining method to draw a full heart
def heart():
  
    # Set the fill color to red
    pen.pencolor('red')
  
    # Start filling the color
    #pen.fillcolor("white)
  
    # Draw the left line
    pen.left(140)
    pen.forward(113)
  
    # Draw the left curve
    curve()
    pen.left(120)
  
    # Draw the right curve
    curve()
  
    # Draw the right line
    pen.forward(112)
  
    # Ending the filling of the color
    pen.end_fill()
  
# Defining method to write text
def txt():
  
    # Move turtle to air
    pen.up()
  
    # Move turtle to a given position
    pen.setpos(0, 0)
  
    # Move the turtle to the ground
    pen.down()
  
    # Set the text color to lightgreen
    pen.color('red')
  
    # Write the specified text in 
    # specified font style and size
    pen.write("Computer Graphics", font=(
      "Verdana", 12, "bold"))

## Panda 
def ring(col, rad):
 
 		# Set the fill
    pen.fillcolor(col)
 
    # Start filling the color
    pen.begin_fill()
 
    # Draw a circle
    pen.circle(rad)
 
    # Ending the filling of the color
    pen.end_fill()

# Draw first ear
pen.up()
pen.setpos(-35, 95)
pen.down
ring('black', 15)
 
# Draw second ear
pen.up()
pen.setpos(35, 95)
pen.down()
ring('black', 15)
 
##### Draw face #####
pen.up()
pen.setpos(0, 35)
pen.down()
ring('white', 40)

##### Draw eyes black #####
 
# Draw first eye
pen.up()
pen.setpos(-18, 75)
pen.down
ring('black', 8)
 
# Draw second eye
pen.up()
pen.setpos(18, 75)
pen.down()
ring('black', 8)

##### Draw eyes white #####
 
# Draw first eye
pen.up()
pen.setpos(-18, 77)
pen.down()
ring('white', 4)
 
# Draw second eye
pen.up()
pen.setpos(18, 77)
pen.down()
ring('white', 4)
 
##### Draw nose #####
pen.up()
pen.setpos(0, 55)
pen.down
ring('black', 5)
 
##### Draw mouth #####
pen.up()
pen.setpos(0, 55)
pen.down()
pen.right(90)
pen.circle(5, 180)
pen.up()
pen.setpos(0, 55)
pen.down()
pen.left(360)
pen.circle(5, -180)

# Draw the heart
pen.up()
pen.setpos(0, 0)
pen.home()
pen.down()
heart()

# Write text
pen.up
pen.down()
pen.home()
pen.setpos(0, 0)
txt()

pen.hideturtle()
