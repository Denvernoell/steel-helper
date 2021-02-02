from sympy import symbols, Eq, solve, pprint
import os
from math import *
def clear(): return os.system("cls")
# clear()


numEqns = int(input("Number of equations: "))
myEqns = []
myVars = []
Eqn = []
# Currently supports 6 eqns. Can add more variables to increase
a, b, c, d, e, f = symbols('a b c d e f')
#Vars = [x, y, z, a, b, c]
Vars = [a, b, c, d, e, f]

i = 1
while i < numEqns+1:
    lhs = input(f"Eqn{i}. left: ")
    rhs = input(f"Eqn{i}. right: ")
    myEqns.append("Eq({},{})".format(lhs, rhs))
    myVars.append(Vars[i-1])
    #mySol1.append("{}={}\n".format(Vars[i-1], "{}"))
    # mySol2.append("solution[{}]".format(Vars[i-1]))
    i = i+1
solution = solve((myEqns), (myVars), dict=True)
# print("\n{}".format(solution))
print(20*"-")
#i = 0
# while i < numEqns:
# print("\n{} = {}".format(myVars[i], solution[myVars[i]]))
#    i = i + 1
pprint(solution)
print("\n" + 20*"-")
