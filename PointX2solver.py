from scipy import optimize
from sympy.solvers import solve
from sympy import Symbol
from sympy import *
x = symbols('x')
def solver(listinput):
    x_2 = []
    for e in range(0, 100):
        def funct(x):
             return sympify(listinput[e])
        
        final_x2 = solve(funct(x))
        x_2.append(final_x2)
    return x_2