# Find remainder when a polynomial involving x is divided by x-k, where k is a real number.

p = int(input("Highest power of x: "))
a = []
for i in range(p+1):
  if i > 1:
a.append(int(input("Coefficient of x^" + str(i) + ": ")))
	if i == 1:
		a.append(int(input("Coefficient of x: ")))
	if i == 0:
		a.append(int(input("Constant: ")))

k = int(input("Value of k: "))

total = 0
for i in range(p+1):
	total += (k**i) * a[i]

print(total)
