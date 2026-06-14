a=int(input("how many students "))
winner={}
for i in range(a):
    key=input("enter the name of student ")
    value=int(input("no of wins "))
    winner[key]=value
print(winner)
    