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
#Values inside of a trig function MUST be in BRACKETS. Trigs CANNOT be in exponents, nor can they have powers.

def derive(expr, var):
    if expr.isdigit():
        return repr(0)
    elif expr == var:
        return repr(1)
    elif trig_finder(expr):
        beginning = expr.index(trig_identify(expr))
        end = expr.index(']')
        expr = expr + ' '
        if '+' in expr[0:beginning] or '+' in expr[end+1:] or '*' in expr[0:beginning] or '*' in expr[end+1:]:
            expr = expr[0:len(expr)-1]
            return special_cases(expr, var, beginning, end)
        return derive_trig(expr, var)
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

#Creates a string of a trig function, and simplifies it if possible.
def make_trig(trig, value):
    if value.isdigit():
        if trig == 'sin':
            return math.sin(math.radians(float(value)))
        elif trig == 'cos':
            return math.cos(math.radians(float(value)))
        elif trig == 'tan':
            return math.tan(math.radians(float(value)))
        elif trig == 'csc':
            return (1/math.sin(math.radians(float(value))))
        elif trig == 'cot':
            return (1/math.tan(math.radians(float(value))))
        elif trig == 'sec':
            return (1/math.cos(math.radians(float(value))))
    return trig + '[' + value + ']'

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

#Derives a trig function. Currently supports sin, cos, tan, cot, csc, sec.
def derive_trig(expr, var):
    beginning = expr.index('[')
    end = expr.index(']')
    if 'sin' in expr:
        return make_product(derive(expr[beginning + 1: end], var), make_trig('cos', expr[beginning + 1: end]))
    elif 'cos' in expr:
        return make_product(derive(expr[beginning + 1: end], var), make_trig('-sin', expr[beginning + 1: end]))
    elif 'tan' in expr:
        return make_product(derive(expr[beginning + 1: end], var), make_trig('sec^2', expr[beginning + 1: end]))
    elif 'cot' in expr:
        return make_product(derive(expr[beginning + 1: end], var), make_trig('-csc^2', expr[beginning + 1: end]))
    elif 'csc' in expr:
        return make_product(derive(expr[beginning + 1: end], var), make_product(make_trig('-csc', expr[beginning + 1: end]), make_trig('cot', expr[beginning + 1: end])))
    elif 'sec' in expr:
        return make_product(derive(expr[beginning + 1: end], var), make_product(make_trig('sec', expr[beginning + 1: end]), make_trig('tan', expr[beginning + 1: end])))
    else:
        raise NameError('Invalid Trig!')

trigs = ['sin', 'cos', 'tan', 'cot', 'sec', 'csc']

#Returns True if the input is in the list of trigs. Otherwise, returns False.
def trig_list(input):
    if input in trigs:
        return True
    return False

#Returns True if one of the trig functions is in the string. Otherwise, returns False.
def trig_finder(string):
    for trig in trigs:
        if trig in string:
            return True
    return False

#Returns the first found trig in a string. If none are found, return None.
def trig_identify(string):
    for trig in trigs:
        if trig in string:
            return trig
    return None

#Handles what operations are inside the brackets and what are outside the brackets.
def special_cases(expr, var, beginning, end):
    expr = expr + ' '
    if expr[beginning - 1] == '*' or expr[end+1] == '*':
        expr = expr[0:len(expr)-1]
        return derive_trig_product(expr[0:end + 1], expr[end+1:], var)
    elif expr[beginning - 1] == '+' or expr[end+1] == '+':
        expr = expr[0:len(expr)-1]
        return derive_trig_sum(expr[0:end + 1], expr[end+1:], var)

def derive_trig_product(expr1, expr2, var):
    print(expr1)
    print(expr2)
    return make_sum(make_product(derive(expr1, var), expr2), make_product(expr1, derive(expr2, var)))

def derive_trig_sum(expr1, expr2, var):
    return make_sum(derive(expr1, var), derive(expr2, var))
