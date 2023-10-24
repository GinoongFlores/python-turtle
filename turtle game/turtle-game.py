import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Turtle Collecting Stars")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turn off automatic screen updates

# Create the player turtle
player = turtle.Turtle()
player.speed(0)
player.shape("turtle")
player.color("skyblue")
player.penup()
player.goto(0, -250)

# Set the player's movement speed
player_speed = 50

# Create stars
stars = []

def create_star():
    star = turtle.Turtle()
    star.speed(0)
    star.color("yellow")
    star.penup()
    star.goto(random.randint(-380, 380), random.randint(300, 600))  # Adjusted y-coordinate range
    stars.append(star)

# Create initial stars
for _ in range(20):
    create_star()

# Function to move the player left
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -380:
        x = -380
    player.setx(x)

# Function to move the player right
def move_right():
    x = player.xcor()
    x += player_speed
    if x > 380:
        x = 380
    player.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")

# Score
score = 0

# Pen for displaying the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Game over condition
game_over = False

# Main game loop
while not game_over:
    wn.update()

    # Move the stars and check for collisions
    for star in stars:
        y = star.ycor()
        y -= 1  # Adjust this value to control the initial falling speed of stars
        star.sety(y)

        # Check for collision with the player
        if player.distance(star) < 20:
            star.goto(random.randint(-380, 380), random.randint(100, 280))
            # Decrease the falling speed after a collision
            y = star.ycor()
            y -= 1  # Adjust this value to change the falling speed after a collision
            star.sety(y)
            score += 10
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

            # Add a new star after catching one
            create_star()

        # Check for game over (if a star reaches the bottom)
        if star.ycor() < -290:
            star.goto(random.randint(-380, 380), random.randint(100, 280))
            # Decrease the falling speed after a collision
            y = star.ycor()
            y -= 1  # Adjust this value to change the falling speed after a collision
            star.sety(y)

            # Show game over message when the last star falls to the bottom
            if len(stars) == 1:
                game_over = True
                break  # Exit the game loop immediately

            # Remove the star from the list when it falls to the bottom
            stars.remove(star)

    # Display game over message
    if game_over:
        game_over_pen = turtle.Turtle()
        game_over_pen.speed(0)
        game_over_pen.color("white")
        game_over_pen.penup()
        game_over_pen.hideturtle()
        game_over_pen.goto(0, 0)
        game_over_pen.write("Game Over!", align="center", font=("Courier", 36, "normal"))

        # Wait for user interaction before closing the window
        wn.update()  # Update the screen to show the game over message

        # Function to close the window when a key is pressed
        def close_window():
            wn.bye()

        # Bind a key press event to close the window
        wn.listen()
        wn.onkeypress(close_window, "space")  # You can change "space" to any key you prefer

# Keep the window open until the user presses a key
wn.mainloop()