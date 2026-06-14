def add(n):
    if n==0:
        return(0)
    else:
        return(n+add(n-1))
def main():
    a=int(input("enter  a number"))
    result=add(a)
    print("sum is",result)
main()

    


    
