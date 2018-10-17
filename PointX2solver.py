from scipy import optimize
from sympy.solvers import solve
from sympy import Symbol
from sympy import *
import numpy as np
x = symbols('x')
def solver(listinput):
    x_2 = []
    for e in range(0, 100):
        def funct(x):
             return sympify(listinput[e])
        final_x2 = solve(funct(x))
        for m in range(0,len(final_x2)-1):
            l = final_x2[m]
            if l <= 0:
                final_x2 = np.delete(final_x2,m)
        x_2.append(final_x2)            
    return x_2
