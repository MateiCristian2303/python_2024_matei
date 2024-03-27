from random import randint
import turtle

number_of_turtles = 20
steps_of_time_number = 100

# Get the dimensions of the screen
screen_width = turtle.window_width()
screen_height = turtle.window_height()

# Create turtles and set their initial positions
pool = [turtle.Turtle(shape='circle') for _ in range(number_of_turtles)]
for unit in pool:
    unit.color('yellow')
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-screen_width//2, screen_width//2), randint(-screen_height//2, screen_height//2))


# Movement of turtles
while True:
    for unit in pool:
        unit.forward(randint(8, 12))

        # Check if the turtle hits the right or left wall
        if unit.xcor() >= screen_width / 2:
            unit.goto(-screen_width//2, randint(-screen_height//2, screen_height//2))

