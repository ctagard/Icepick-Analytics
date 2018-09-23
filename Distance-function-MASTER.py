#Cole Agard
#Icepick Analytics MASTER 
#9/23/2018
from numpy import *
from sympy import *
from scipy import *
from Normal_functionfinder import normal
x, y, z = symbols("x y z") #Define the symbols that we will be using

functionone = input("What is the first function? Please use 'y' when typing symbolic equation ") #f(x), user defined
print("f(x) =  " + functionone + " ")
functiontwo = input("What is the second function? Please use 'y' when typing symbolic equation ")#g(x), user defined

print("g(x) = " + functiontwo + "")
function1real = sympify(functionone)

function2real = sympify(functiontwo)

print(normal(function1real))
