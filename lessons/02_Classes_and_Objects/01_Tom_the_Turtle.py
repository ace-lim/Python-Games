""" Turtle in Pygame

We really miss the turtle module from Python's standard library. It was a great
way to introduce programming, so let's make something similar in PyGame, using
objects. 

This program is for assignment 3 and 4

Assignment 3:

1. Read and run the program `01_Tom_the_Turtle.py` in this lession directory.
2. Create a derived class from the `Turtle` class that adds some new behavior.
   Add a function `right` that turns the turtle to the right. ( Bonus, use the
   `left` function to implement the `right` function )
3. In your derived class, add a new variable `color` and a way to set it. Use
   that color to set the color of the turtle's line
4. Add a `pen_up` and `pen_down` function that will raise and lower the pen.

Assignment 4:

1. Create a function ( not a method, the function should not be part of a class) 
   in your `01_Tom_the_Turtle` program that takes a Turtle object and prints
   out the x and y position of the turtle.
2. Show that your function works by creating a turtle, moving it around, and
   then calling your function, for both the base `Turtle` class and your derived
   class.


"""
import math
import pygame

pen_down=True

def event_loop():
    """Wait until user closes the window"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

class Turtle:
    def __init__(self, screen, x: int, y: int):
        self.x = x
        self.y = y
        self.screen = screen
        self.angle = 0  # Angle in degrees, starting facing right

    def forward(self, distance):
        # Calculate new position based on current angle
        radian_angle = math.radians(self.angle)

        start_x = self.x  # Save the starting position
        start_y = self.y

        # Calculate the new position displacement
        dx = math.cos(radian_angle) * distance
        dy = math.sin(radian_angle) * distance

        # Update the turtle's position
        self.x += dx
        self.y -= dy

        
    
        pygame.draw.line(self.screen, black, (start_x, start_y), (self.x, self.y), 2)
        # Draw line to the new position
        #pygame.draw.line(self.screen, black, (start_x, start_y), (self.x, self.y), 2)

    def left(self, angle):
        # Turn left by adjusting the angle counterclockwise
        self.angle = (self.angle + angle) % 360

    def right(self, angle):
        self.angle = (self.angle - angle) % 360

class Right(Turtle): 
    def __init__(self, screen, x: int, y: int, color=(255, 0, 0)):
        super().__init__(screen, x, y)
        self.color = color
        self.pen = True
    def colors(self, color):
        self.color = color
    def pen_up(self):
        self.pen=False
    def pen_down(self):
        self.pen=True


    def forward(self, distance):
        # Calculate new position based on current angle
        radian_angle = math.radians(self.angle)

        start_x = self.x  # Save the starting position
        start_y = self.y

        # Calculate the new position displacement
        dx = math.cos(radian_angle) * distance
        dy = math.sin(radian_angle) * distance

        # Update the turtle's position
        self.x += dx
        self.y -= dy

        if self.pen:
            pygame.draw.line(self.screen, self.color, (start_x, start_y), (self.x, self.y), 2)


        
def get_x_y(turtle: Turtle):
    print({turtle.x}, {turtle.y})


# Main loop

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Turtle Style Drawing")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 100, 255)

screen.fill(white)



turtle = Right(screen, screen.get_width() // 2, screen.get_height() // 2)  # Start at the center of the screen

#turtle.pen_up()
get_x_y(turtle)

for _ in range(3):
    
    turtle.forward(200)  # Move forward by 100 pixels
    turtle.left(120)  # Turn left by 90 degrees

get_x_y(turtle)

turtle.pen_up()
turtle.colors(blue)
turtle.right(90)
turtle.forward(100)
turtle.pen_down()
for _ in range(100000):
    turtle.forward(1)
    turtle.right(1)
turtle.pen_up()
turtle.forward(100)
turtle.pen_down()
turtle.colors(black)
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

get_x_y(turtle)

# Display the drawing
pygame.display.flip()

# Wait to quit
event_loop()

# Quit Pygame
pygame.quit()
