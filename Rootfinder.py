from sympy import *
from numpy import *
from scipy import optimize
from scipy import *
from scipy.optimize import fsolve
import numpy as np

def root_finder(input1, function2):                    #Inputs are the array results, and the function we are trying to solve WITH
    results_root = []   
    print(len(input1))
    x, y, z = symbols('x y z')                               #Create array with values coming from the solution outlined in the loop
    for i in range(0, 100):
        beta = input1[i]

        alpha = sympify(beta)

        gamma = sympify(function2.subs(y,x))
        def c(x):
            return (gamma - alpha)
        results_root.append(c(x))        #Solve EACH instance of this equation and ouput this to the array above
    return results_root;


