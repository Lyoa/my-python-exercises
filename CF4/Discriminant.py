#math module - sqrt import
from math import sqrt

a = float(input("Enter value for A: "))
b = float(input("Enter value for B: "))
c = float(input("Enter value for C: "))

#given formula
#(-B + sqrt(B^2 - 4AC)) / (2A)
#(-B - sqrt(B^2 - 4AC)) / (2A)
#-C/B !!!
#B^2 - 4AC : != if D = neg, !1 = if D = pos

D = b ** 2 - 4 * a * c

if a == 0 and b == 0:
    print("No unknown")
elif a == 0 and b > 0:
    print(f"Solution: {-c / b:.3f}") #stringformat (new way) to 3 decimal places
else:
    if D < 0:
        print("No solutions")
    else:
        first_sol = (-b + sqrt(D))/(2 * a)
        if D > 0:
            second_sol = (-b - sqrt(D))/(2 * a)
            print(f"Solutions: {first_sol:.3f}") and ("{second_sol:.3f}") #stringformat (new way) to 3 decimal places
        elif D == 0:
            print(f"Solution: {first_sol:.3f}")

#recheck formula and computation - failed in quiz!
