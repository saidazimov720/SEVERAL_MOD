import math
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b !=0:
        return a/b
    else:
        return "cannot divide to the zero"
    
def pow(a,b):
    return a ** b

def square(a):
    try:
        result = math.sqrt(a)
        return result
    except ValueError as e:
        return f"error:{e}"
