'''
Sydnee Larson 
I created a house scene with a sun and tree. I made sure to include a small window and a door.
I also wanted to include a flower on the left side of the house. 

'''


# loads the Turtle graphics module, which is a built-in library in Python
import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()



def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    
    Parameters:
    - t: turtle object
    - length: total length of the curve
    - curve_factor: positive for upward curve, negative for downward curve
    - segments: number of segments (higher = smoother curve)
    - fill_color: optional color to fill if creating a closed shape
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        
    segment_length = length / segments
    # Save the original heading
    original_heading = t.heading()
    
    for i in range(segments):
        # Calculate the angle for this segment
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)  # Reset the angle for the next segment
    
    # Reset to original heading
    t.setheading(original_heading)
    
    if fill_color:
        t.end_fill()
        
def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()


#YOU MUST add function calls in this draw_scence function defintion
# to create your scence (No statements outside of function definiions)
def draw_scene(t):
    """Draw a colorful scene with various shapes"""
    # Set background color
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    #Ground# 
    jump_to(t, -400, -100)
    draw_rectangle(t, 800, 270, "green")

    #Sun# 
    jump_to(t, 150, 150 )
    draw_circle(t, 60, "yellow")

    #House# 
    jump_to(t, -200, 0)
    draw_square(t, 100, "pink")

    #Roof# 
    jump_to (t, -200, 0)
    draw_triangle(t, 100, "red")

    #Door# 
    jump_to(t, -165, -50)
    draw_rectangle(t, 30, 50, "purple")

    #Window# 
    jump_to(t, -150, -35)
    draw_circle(t, 12, "lightblue")

    #Tree Trunk# 
    jump_to(t, 100, -40)
    draw_rectangle(t, 20, 60, "saddlebrown")

    #Tree Leaves#
    jump_to(t, 113, -50)
    draw_circle(t, 40, "forestgreen")

    #Flower# 
    jump_to(t, -250, -60)
    
    #stem#
    draw_rectangle(t, 5, 40, "lightgreen")

    #petals#
    flower_color = "red"
    t.color(flower_color)
    for _ in range(6):
        t.circle(10)
        t.right(60)
    #center#
    t.color("yellow")
    t.begin_fill()
    t.circle(5)
    t.end_fill()



# This is the main() function that starts off the execution
def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

# if this script is executed, call the main() function
# meaning when is file is run directly
if __name__ == "__main__":
    main()