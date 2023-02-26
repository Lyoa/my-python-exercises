def gcd(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return gcd(b, c)

def calculate(a, b):
    return gcd(a, b)