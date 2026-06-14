def check_divisible(a, b):
    if a % b == 0:
        print("First number is divisible by second number")
    else:
        print("First number is not divisible by second number")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
check_divisible(num1, num2)