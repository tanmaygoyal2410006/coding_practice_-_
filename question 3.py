num=list(map(int,input("enter the elements of list ").split()))
print(num)
target=int(input("enter the target "))
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==target:
            print("the indices are ",i," and ",j)