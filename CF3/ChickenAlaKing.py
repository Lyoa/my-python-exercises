import math
v0 = float(input("Initial Velocity: "))
AngleInDegrees = float(input(" Angle: "))
time = float(input("Time: "))
g = 9.8

radian = AngleInDegrees * (math.pi / 180.0)

x = v0 * math.cos(radian) * time
y = v0 * math.sin(radian) * time - 0.5 * g * time**2

print(f"{x:.0f}, {y:.0f}")