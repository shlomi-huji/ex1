#################################################################
# FILE : hello_turtle.py
# WRITER : Shlomi Rybalov , shlomirybalov , 325926137
# EXERCISE : intro2cs2 ex1 2023
# DESCRIPTION: A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH: Bugs Bunny, b_bunny.
#								 	      Daffy Duck, duck_daffy.
# WEB PAGES I USED: www.looneytunes.com/lola_bunny
# NOTES: ...
#################################################################
import turtle

# These next lines draw a triangle
def draw_triangle():

    for i in range(3):
        turtle.forward(45)
        turtle.right(120)

# These next lines draw a sail
def draw_sail():

    turtle.left(90)
    turtle.forward(50)
    turtle.right(150)
    draw_triangle()
    turtle.right(30)
    turtle.up()
    turtle.forward(50)
    turtle.down()
    turtle.left(90)

# These next lines draw a ship
def draw_ship():

    turtle.right(90)
    turtle.forward(50)
    for i in range(3):
        draw_sail()
        turtle.forward(50)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(180)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(30)

# These next lines draw a fleet
def draw_fleet():

    turtle.left(90)
    draw_ship()
    turtle.left(90)
    turtle.up()
    turtle.forward(300)
    turtle.down()
    turtle.right(90)
    draw_ship()
    turtle.right(90)
    turtle.up()
    turtle.forward(300)
    turtle.down()

if __name__ == "__main__" :

    draw_fleet()

    turtle.done()

