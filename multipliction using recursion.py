def multiply(num):
    if num == 0:
        return 1
    else:
        return num * multiply(num - 1)
def main():
    a = int(input("Enter a number: "))
    result = multiply(a)
    print("Multiplication is", result)

main()
    
