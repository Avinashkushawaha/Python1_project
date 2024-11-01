def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(x, -n)
    else:
        return x * power(x, n - 1)
base = float(input("Enter the base number (x): "))
exponent = int(input("Enter the exponent (n): "))
result = power(base, exponent)
print(f"{base} raised to the  power of  {exponent} is {result}")    