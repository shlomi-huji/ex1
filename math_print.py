#################################################################
# FILE : math_print.py
# WRITER : your_name , your_login , your_id
# EXERCISE : intro2cs2 ex1 2023
# DESCRIPTION: A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH: Bugs Bunny, b_bunny.
#								 	      Daffy Duck, duck_daffy.
# WEB PAGES I USED: www.looneytunes.com/lola_bunny
# NOTES: ...
#################################################################
import math


def golden_ratio():
    print((1+math.sqrt(5))/2)


def six_squared():
    print(math.pow(6, 2))


def hypotenuse():
    print(math.sqrt(5*5+12*12))


def pi():
    print(math.pi)


def e():
    print(math.e)

def squares_area():
    print(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)


if __name__ == "__main__":

    golden_ratio()

    six_squared()

    hypotenuse()

    pi()

    e()

    squares_area()
