def exponent(a, b):
    prod = 1
    for i in range(b):
        prod = prod * a
    return prod
num1 = int(input("Enter a base: "))
num2 = int(input("Enter the exponent: "))
c = exponent(num1, num2)
print(c)