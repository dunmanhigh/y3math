# Intersection of linear equations

a = float(input("Enter a, b for y = ax + b: "))
b = float(input())
c = float(input("Enter c, d for y = cx + d: "))
d = float(input())

if a == c:
    print("No intersection")
else:
    m = (d - b) / (a - c)
    n = a * m + b
    print("coordinate of intersection is (", m, ",", n, ")")
