a=int(input("enter a number between 0-999  "))
if a<0:
    print("invalid")
elif a<10:
    print("one digit")
elif a<100:
    print("two digit")
elif a<=999:
    print("three digit")
else:
    print("invalid")
                    