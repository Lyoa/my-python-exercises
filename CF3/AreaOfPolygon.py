from math import tan, pi

NumSides = float(input("Number of sides: "))
LenSides = float(input("Length of sides: "))

PolyArea = ( LenSides * NumSides * NumSides ) / (4 * tan(pi / LenSides))
print(f"{PolyArea:.2f}")