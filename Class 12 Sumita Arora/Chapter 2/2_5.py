t=tuple(input("enter the elements of tuple "))
a=input("enter the element to be searched ")
for i in range(len(t)):
    if t[i]==a:
        print("element found at index ",i)
        break
    else:
        print("element not found")     