#Cole Agard
#function that determines ALL equations normal to f(x), represented by function1
#To change number of equations, change the top bound of the range in line 17
from sympy import *
from numpy import *
import numpy as np
from scipy import *
from sympy import diff

x, y, z = symbols("x y z")
init_printing(use_unicode=True)


def normal(function1):
    a = (-1/diff(function1, y)) * x + (function1 + y/diff(function1, y))
    results = []
    for i in range(1, 101):
        j = a.subs(y, i)
        results.append(a.subs(y, i))
return results;

