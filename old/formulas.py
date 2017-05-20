import math
import numbers

#Finds the roots of a quadratic equation in the form of ax^2 + bx + c = 0.
def quadratic(a, b, c):
    try:
        if (b**2 - (4 * a * c)) < 0:
            print("Imaginary roots!")
            return None, None
    except TypeError:
        print("Invalid inputs!")
        return None, None
    result = ((-1 * b) - (math.sqrt(b**2 - (4 * a * c))))/(2 * a)
    result2 = ((-1 * b) + (math.sqrt(b**2 - (4 * a * c))))/(2 * a)
    print("Root 1: " + repr(result) + " Root 2: " + repr(result2))
    return result, result2


#Function that derives simple single variable expressions that have summation, multiplication, and/or exponentiation.
#Expressions should be as simplified as possible before applying function.
#Everything must be entered as strings. Must denote multiplication explicitly.
#Do NOT use multiplication for variables with powers. Use a carrot instead.
#Values in an exponent MUST be in parentheses. Powers CANNOT have variables.

def derive(expr, var):
    if expr.isdigit():
        return repr(0)
    elif expr == var:
        return repr(1)
    elif '+' in expr:
        return derive_sum(expr, var)
    elif '*' in expr:
        return derive_product(expr, var)
    elif '^' in expr:
        return derive_exp(expr, var)

    else:
        return "invalid equation/variable"

#Creates a string of a summation, and simplifies it if possible.
def make_sum(a, b):
    if a == None and b == None:
        return repr(0)
    if a == None:
        return b
    if b == None:
        return a
    if a.isdigit():
        if float(a) == 0:
            return b
    if b.isdigit():
        if float(b) == 0:
            return a
    if a.isdigit() and b.isdigit():
        return repr(float(a) + float(b))
    else:
        return a + "+" + b

#Creates a string of a multiplication, and simplifies it if possible.
def make_product(a, b):
    if a == None:
        return repr(0)
    if b == None:
        return repr(0)
    if a.isdigit():
        if float(a) == 0:
            return repr(0)
        elif float(a) == 1:
            return b
    if b.isdigit():
        if float(b) == 0:
            return repr(0)
        elif float(b) == 1:
            return a
    if a.isdigit() and b.isdigit():
        return repr(a*b)
    else:
        return a + "*" + b

#Creates a string of a exponentiation, and simplifies it if possible.
def make_exp(base, e):
    if base == None:
        return repr(0)
    if e == None:
        return repr(1)
    if base.isdigit():
        if float(base) == 0:
            return 0
        elif float(base) == 1:
            return 1
        else:
            return base**e
    else:
        return base + "(" + e + ")"

#Derives a summation.
def derive_sum(expr, var):
    cutoff = expr.index('+')
    return make_sum(derive(expr[0:cutoff], var), derive(expr[cutoff + 1:], var))

#Derives a product.
def derive_product(expr, var):
    cutoff = expr.index('*')
    return make_sum(make_product(derive(expr[0:cutoff], var), expr[cutoff + 1:]), make_product(expr[0:cutoff], derive(expr[cutoff + 1:], var)))

#Derives an exponent.
def derive_exp(expr, var):
    beginning = expr.index('(')
    end = expr.index(')')
    #Debugging
    """print(expr[beginning + 1:end])
    print(make_exp(expr[0:beginning], repr(float(expr[beginning + 1:end]) - 1)))
    print(make_product(expr[beginning + 1:end], make_exp(expr[0:beginning], repr(float(expr[beginning + 1:end]) - 1))))"""
    return make_product(expr[beginning + 1: end], make_exp(expr[0:beginning], repr(float(expr[beginning + 1: end]) - 1)))

#Prints the formula needed to calculate arclength, given a formula yet to be derived.
#Formula must be a string, and must follow the rules of the derive function.
def arclength(formula, var):
    print("sqrt(1+(" + derive(formula, var) + ")^2)")

#Prints values required for Astro Lab.
def lab(observed, size):
    redshift = (observed - 6562.8)/6562.8
    print("redshift: " + str(redshift) + "Angstroms")
    speed = redshift * 3 * 10**5
    print("velocity: " + str(speed) + "km/s")
    milliradians = size * (4.4/6.6)
    print("mrad: " + str(milliradians) + "mrad")
    distance = 22/milliradians
    print("distance: " + str(distance) + "Mpc")
