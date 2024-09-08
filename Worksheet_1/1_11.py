import math

x1,y1=map(int,input("Enter the coordinates of the first point: ").split())
x2,y2=map(int,input("Enter the coordinates of the second point: ").split())

Distance=math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"The Euclidean distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {Distance}")