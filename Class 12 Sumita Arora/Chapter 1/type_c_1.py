def check_number(x):
    if x < 0:
        print("negative")
    elif x == 0:
        print("zero")
    else:
        print("positive")
x = int(input("Enter a number: "))
check_number(x)
