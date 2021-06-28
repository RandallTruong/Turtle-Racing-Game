# The turtle module allow you to perform basic 2d graphics
import turtle
import time
import random

WIDTH, HEIGHT = 500, 500

# Color of racers
COLORS = ["magenta", "brown", "skyblue", "black",
          "navy", "orange", "violet", "gold", "pink", "gray"]


def get_number_of_turtles():  # Ask user to input the number of turtles they want to race
    number_of_turtles = 0
    # Continue to ask the user to insert a number until they insert a valid number
    while True:
        number_of_turtles = input(
            "Enter the number of turtles to race (2-10): ")
        # Check to see if input is number
        if number_of_turtles.isdigit():
            # converts numeric string to int
            number_of_turtles = int(number_of_turtles)
        else:
            print("Invalid entry please try again")
            # Returns to the start of the while loop (does not execute code afterwards)
            continue
        if 2 <= number_of_turtles <= 10:
            return number_of_turtles
        else:
            print("Invalid entry number is not in range")


turtles = get_number_of_turtles()
# Randomize the list of colors
random.shuffle(COLORS)
# Slice opertor: Select unique colors based on the number of turtles
colors = COLORS[:turtles]


def create_turtles(colors):
    # Create an empty list to hold all the turtles
    turtles = []
    # Spacing of each turtle
    spacingx = WIDTH / (len(colors) + 1)
    # Loop through all the colors  and create a turtle for every  color
    # Enumerate gives the index and the value of all the elements in colors
    for i, color in enumerate(colors):
        # Create a turtle
        racer = turtle.Turtle()
        # Set the color of the turtle to the current color in the for loop
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        # Removes the line drawn when the turtle moves
        racer.penup()
        # Setting Position
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        # Add turtle to list
        turtles.append(racer)
    return turtles


def race(colors):
    turtles = create_turtles(colors)
    # Turtle keeps moving until one reaches the end of the screen
    while True:
        for racer in turtles:
            # Minimum and maximum amount the turtle moves at every iteration
            # Turtles moves a random range between 1 and 20 pixels
            distance = random.randrange(1, 20)
            racer.forward(distance)

            # Gives the position of this turtle
            x, y = racer.pos()
            # Check if racer is past the finish line
            if y >= HEIGHT // 2 - 10:
                # return the winning color turtle
                # Find the index of the turtle that was the winner
                # then use the same index to find the color in the list
                return colors[turtles.index(racer)]


def init_window():
    # Initialize a screen with the turtle module
    window = turtle.Screen()
    window.title("Turtle Racing Game by Randall Truong")
    # Define a background color
    window.bgcolor("green")
    # Define width and height of screen
    window.setup(width=500, height=500)


init_window()
winning_turtle = race(colors)
print(f"The winning turtle is {winning_turtle.upper()}!!!")

# Waits 5 seconds before closing the program
time.sleep(5)
