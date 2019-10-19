# Trigonometry values

import numpy as np

a = float(input("For a*sin/cos/tan(bx+c), enter the value of a, b, and c: "))
b = float(input())
c = float(input())

ang = input("Angle in degrees: ")

ang = float(ang) * 2 * np.pi / 360

ans_sin = a * np.sin(b * ang + c)
ans_cos = a * np.cos(b * ang + c)
ans_tan = a * np.tan(b * ang + c)

print("sin:", ans_sin)
print("cos:", ans_cos)
print("tan:", ans_tan)
