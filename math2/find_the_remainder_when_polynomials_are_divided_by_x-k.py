# Print the remainder when a polynomial about x is divided by x-k, where k is a real number

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

print(sum);
