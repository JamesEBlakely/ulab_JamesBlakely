# File: quadratic.py

import numpy as np

def discriminant(a,b,c):
    # Finds the discriminant of the quadratic equation ax^2+bx+c=0
    discriminant = b**2 - (4*a*c)
    return(discriminant)

def vertex(a,b,c):
    # finds the vertex of the parabola defined by ax^2+bx+c
    vertex = -1*b/(2*a)
    return(vertex)

def solve_quadratic(a,b,c,discriminant,vertex):
    # solves the quadratic equation ax^2+bx+c=0
    if discriminant > 0:
        pos_x = (-b+np.sqrt(discriminant))/(2*a)
        neg_x = (-b-np.sqrt(discriminant))/(2*a)
        return(pos_x,neg_x)
    elif discriminant == 0:
        x = vertex
        return(x)
    else:
        return(False)

