
from sympy import *
from scipy import *
from Normal_functionfinder import normal
from Definitionsfunctions import functionone,functiontwo
from Rootfinder import root_finder
from PointX2solver import solver
from finalDistance import final_distance

def distance(function1, function2):
    x, y, z = symbols("x y z")
    a = str(function1)
    b = str(function2)
    function1real = sympify(a)
    function2real = sympify(b)
    def funct1(y):
        return sympify(a)
    def funct2(y):
        return sympify(b)

    allnormallines = normal(function1real)
    print(allnormallines)
    solutionsofroots = root_finder(allnormallines, function2real)
    x2 = solver(solutionsofroots)
    finaldistance = final_distance(x2,funct1(y),funct2(y))
    print(finaldistance)
