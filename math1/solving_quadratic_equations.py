# Determine if a quadratic equation has no, equal or distinct roots

import math

# Get coefficients of x^2, x and constant
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a > 0);
  print("Positive")
elif (a < 0);
  print("Negative")

if (b*b - 4*a*c < 0):
  print("No real roots")
elif (b*b - 4*a*c == 0): # equal roots
  print(-b/(2*a))
else: # (b*b - 4*a*c > 0) i.e. distinct roots
  print((-b+math.sqrt(b*b-4*a*c))/(2*a), (-b-math.sqrt(b*b-4*a*c))/(2*a))
