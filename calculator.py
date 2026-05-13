def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def multiply(a, b):
    return a * b
def power(a, b):
    c = 1
    for i in range(b):
        c*=a
    return c