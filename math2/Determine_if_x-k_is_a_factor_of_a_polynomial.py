# Determine if x-k is a factor of a polynomial by Factor Theorem

p = int(input("Highest power of x: "))
a = []
for i in range(0, p+1):
	if (i > 1):
		a.append(int(input("coefficient of x^"+str(i)+": ")))
	if (i == 1):
		a.append(int(input("coefficient of x: ")))
	if (i == 0):
		a.append(int(input("constant: ")))

k = int(input("Value of k: "));
sum = 0;
for i in range(0, p+1):
	sum += (k**i)*a[i];

if (sum == 0):
	print("Yes")
else:
	print("No")
