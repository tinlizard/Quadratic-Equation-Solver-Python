import cmath

a = float(input("please enter an integer value for a"))
b = float(input("please enter an integer value for b"))
c = float(input("please enter an integer value for c"))
disc = cmath.sqrt(b**2-4*a*c)

def quadraticEquationSolver():
    x_one = (-b+disc)/(2*a)
    x_two = (-b-disc)/(2*a)
    print(str(x_one))
    print(str(x_two))

quadraticEquationSolver()
