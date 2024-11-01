def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = int(input("enter a number here: "))    
b = int(input("enter a another number: " ))
result = gcd (a, b)
    
print(f"The gcd of {a} and {b} is {result}")
