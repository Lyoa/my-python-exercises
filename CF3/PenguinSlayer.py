import math

def d(x1, y1, x2, y2) :
  return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

xA = float(input("X coordinate of archer: "))
yA = float(input("Y coordinate of archer: "))
xP = float(input("X coordinate of penguin: "))
yP = float(input("Y coordinate of penguin: "))

d = d(xA, yA, xP, yP)
print(f"{d:.2f}")