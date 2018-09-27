#Cole Agard
#Icepick Analytics MASTER 
#9/23/2018
from numpy import *
from sympy import *
from scipy import *
from Normal_functionfinder import normal
from Definitionsfunctions import functionone,functiontwo
from Rootfinder import root_finder
from PointX2solver import solver
from finalDistance import final_distance
x, y, z = symbols("x y z") #Define the symbols that we will be using

a = str(functionone())
b = str(functiontwo())
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

