l=list(map(int,input("enter the elements of list ").split()))
m=list(map(int,input("enter the elements of list ").split()))
n=[]
sum=0
for i in range(len(l)):
        sum=l[i]+m[i]
        n.append(sum)
print(n)
