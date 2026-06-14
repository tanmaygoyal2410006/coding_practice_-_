def multiply(a,b):
    sum=0
    for i in range(0,b):
        sum=sum+a
    return sum
num1=int(input("enter number first"))
num2=int(input("enter number two"))
c=multiply(num1,num2)    
print(c)