def roots(a,b,c):
    """cuadratica"""
    discriminant=b**2-4*a*c
    
    #x= f"({(-b) +math.sqrt(discriminant)/(2*a)})"
    #y= f"({(-b) -math.sqrt(discriminant)/(2*a)})"
    
    if discriminant<0:
        return "()"
    elif discriminant==0:
        return "("+ -b/(2*a) +")"
    else:
        return f"({(-b) +math.sqrt(discriminant)/(2*a)}) , ({(-b) -math.sqrt(discriminant)/(2*a)})"

def value_y(a,b,c,x):
    return a*(x**2)+b*x+c
 
def to_strings(a,b,c):
    return f"f(x) = {a} * X^2 + {b} * X + {c}"
def derivation(a, b, c):
    return f"f'(x) = {a*2}* X + {b}"
