# import math

# def calculate(n, r):
#     ways = math.comb(n, r)
#     return ways

# n = 58
# r = 6
# result = calculate(n, r)
# print("1 in " + str(result))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# def calculate(n, r):
#     return factorial(n) / (factorial(r) * factorial(n-r))

# n = 58
# r = 6
# result = int(calculate(n, r))
# print(f"1 in {result}")

# def calculate(n, r):
#     ways = factorial(n) / (factorial(r) * factorial(n-r))
#     return int(ways)

# # def factorial(number):
# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         return x * factorial(x-1)

# n = 58
# r = 6
# result = calculate(n, r)
# print("1 in " + str(result))

def calculate(n, r):
    ways = factorial(n) / (factorial(r) * factorial(n - r))
    return '1 in ' + str(int(ways)) #task reqm int(), include '1 in'

# def factorial(number/x):
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


