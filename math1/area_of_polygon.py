import numpy as np

num = int(input("Number of edges of polygon: "))

cx = []
cy = []
print("Enter the coordinates of each point of the polygon anticlockwise: ")
for a in range(num):
    cx.append(float(input()))
    cy.append(float(input()))

area = 0.0
for a in range(num):
    area += cx[a - 1] * cy[a] - cx[a] * cy[a - 1]
area = np.abs(area / 2)
print(area)
