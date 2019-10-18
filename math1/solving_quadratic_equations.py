# Determine if a quadratic equation has no, equal or distinct roots

import math

# Get coefficients of x^2, x and constant
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (b**2 - 4a*c < 0):
  print("No real roots")
elif (b**2 - 4a*c == 0): # equal roots
  print(-b/(2a))
else: # (b*b - 4*a*c > 0) i.e. distinct roots
  print((-b+math.sqrt(b**2-4a*c))/(2a)) #quadratic formula
  print((-b-math.sqrt(b**2-4a*c))/(2a))
