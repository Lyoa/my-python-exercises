# from math import gcd

# def reduce(num, den):
#     common_divisor = gcd(num, den)
#     new_num = num // common_divisor
#     new_den = den // common_divisor
#     return (new_num, new_den)

# def display(num, den):
#     new_num, new_den = reduce(num, den)
#     return f"({num})/({den}) can be reduced to ({new_num})/({new_den})"

# print(display(10, 20))

# from math import gcd

# def reduce(num, den):
#     divisor = gcd(num, den)
#     new_num = num // divisor
#     new_den = den // divisor
#     return (new_num, new_den)

# def display(num, den):
#     new_num, new_den = reduce(num, den)
#     return f'({num})/({den}) can be reduced to ({new_num})/({new_den})'

# print(display(10, 20))

# def gcd(n,m):
#     d = min(n,m)
#     while n % d != 0 or m % d != 0:
#         d = d - 1
#     return d

# def reduce(num, den):
#     if num == 0:
#         return (0,1)
#     g = gcd(num,den)
#     return (num // g , den // g)

# def display(num, den):
#     (n,d) = reduce(num,den)
#     return (n,d)

def gcd(n,m):
    d = min(n,m)
    while n % d != 0 or m % d != 0:
        d = d - 1
    return d

def reduce(num, den):
    g = gcd(num, den)
    return (num // g, den // g)

def display(num, den):
    new_num, new_den = reduce(num, den)
    return f'({num})/({den}) can be reduced to ({new_num})/({new_den}).'
#return f'{num}/{den} can be reduced to {new_num}/{new_den}.'
print(display(10,20))
