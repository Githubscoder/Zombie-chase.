

import random
import turtle
import time

# Initialize the screen
screen = turtle.Screen()
screen.bgcolor('light blue')  # Set initial background color
screen.register_shape("Zombie.gif")
screen.register_shape("Player.gif")


# Define time variables
day_duration = 60  # Duration of a full day in seconds
current_time = 0  # Current time in the day-night cycle

# Define colors for different times of day
day_colors = {
    'morning': 'light blue',
    'afternoon': 'blue',
    'evening': 'dark blue',
    'night': 'black'
}

# Function to update the background color
def update_background():
    global current_time  # Make sure to use the global variable
    if 0 <= current_time < day_duration / 4:
        screen.bgcolor(day_colors['morning'])
    elif day_duration / 4 <= current_time < day_duration / 2:
        screen.bgcolor(day_colors['afternoon'])
    elif day_duration / 2 <= current_time < 3 * day_duration / 4:
        screen.bgcolor(day_colors['evening'])
    else:
        screen.bgcolor(day_colors['night'])


# Create the player turtle
player = turtle.Turtle()
player.speed("normal")
player.shape("Player.gif")
player.penup()

# Create the zombie turtle
zombie = turtle.Turtle()
zombie.shape('Zombie.gif')
zombie.penup()

# Initialize the heading (0 degrees)
heading = 0

# Define functions for movement
def move_forward():
    player.setheading(90)  # Set the turtle to face upward
    player.forward(10)

def move_backward():
    player.setheading(-90)  # Set the turtle to face downward
    player.forward(10)

def turn_left():
    global heading
    if heading == 0:
        player.setheading(180)  # Set the turtle to face left
        player.forward(10)
    else:
        player.forward(10)

def turn_right():
    global heading
    if heading == 0:
        player.setheading(0)  # Set the turtle to face right
        player.forward(10)
        heading = 0
    else:
        player.forward(10)

def move_zombie():
    # Get the current position of the player
    player_pos = player.pos()
    # Set the zombie's heading towards the player's position
    zombie.setheading(zombie.towards(player_pos))
    # Move the zombie forward by a fixed amount
    zombie.forward(20)

def check_collision():
    if player.distance(zombie) < 20:
        print("Collision! Zombie got you!")
    


# Bind arrow keys to movement functions
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")

# Listen for key presses
screen.listen()

# Main game loop
while True:
    move_zombie()
    check_collision()
    
    # Update the time
    current_time += 1
    if current_time >= day_duration:
        current_time = 0  # Reset the cycle
    
    # Update the background color
    update_background()
    
    # Sleep for a bit to slow down the cycle for visibility
    time.sleep(1)

# Close the turtle graphics window when done
turtle.done()

