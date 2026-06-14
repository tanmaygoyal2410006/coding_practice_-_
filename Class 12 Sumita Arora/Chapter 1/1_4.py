a=int(input("enter a number"))
if a<0 or a>999:
    print("invalid")
else:
    if a<10:
        print("one digit")
    else:
        if a<100:
            print("two digit")
        else:
            print("three digit")