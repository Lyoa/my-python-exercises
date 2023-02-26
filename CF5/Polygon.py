import math

perimeter = 0
area = 0
xAxis = []
yAxis = []

while True:
    x =input("Enter x input: ")
    if x == "stop":
        break
    else:
        x = float(x)
        xAxis.append(x) #to add another item
        y = input("Enter y input: ")
        y = float(y)
        yAxis.append(y)

for i in range(len(xAxis)):
    if i == (len(xAxis) - 1):
        area += (xAxis[-1] * yAxis[0] - xAxis[0] * yAxis[-1])
        distance = math.sqrt((xAxis[-1] - xAxis[0]) ** 2 + (yAxis[-1] - yAxis[0]) **2)
        perimeter += distance
    else: #opposite
        area += (xAxis[i] * yAxis[i+1] - xAxis[i+1] * yAxis[i])
        distance = math.sqrt((xAxis[i+1] - xAxis[i]) ** 2 + (yAxis[i+1] - yAxis[i]) ** 2)
        perimeter += distance

area = abs(area/2) #absolute value
print(f'''Perimeter: {perimeter:.2f}
Area: {area:.2f}
''') #end of multi-line

# class Point:
#     def init(self, x, y):
#         self.x = x
#         self.y = y

# class Polygon:
#     def init(self):
#         self.points = []
#         self.perimeter = 0
#         self.area = 0

# def distance(p1, p2):
#     return ((p1.x - p2.x), 2 + (p1.y - p2.y), 2) ** 0.5

# polygon = Polygon()

# x = input("Enter x coordinate of first point: ")
# while x != "stop":
#     y = float(input("Enter y coordinate of first point: "))
#     point = Point(float(x))
#     polygon.points.append(point)
#     if len(polygon.points) > 1:
#         prev_point = polygon.points[-2]
#         d = distance(point, prev_point)
#         polygon.perimeter += d
#     x = input("Enter x coordinate of next point (or 'stop' to finish): ")

# if len(polygon.points) > 2:
#     # Add distance between last and first points to perimeter
#     first_point = polygon.points[0]
#     last_point = polygon.points[-1]
#     d = distance(first_point, last_point)
#     polygon.perimeter += d

#     # Calculate area of polygon using Shoelace Theorem
#     for i in range(len(polygon.points)):
#         p1 = polygon.points[i]
#         p2 = polygon.points[(i+1) % len(polygon.points)]
#         polygon.area += p1.x * p2.y - p2.x * p1.y
#     polygon.area = abs(polygon.area) / 2

# print(f"Perimeter: {polygon.perimeter:.2f}")
# print(f"Area: {polygon.area:.2f}")