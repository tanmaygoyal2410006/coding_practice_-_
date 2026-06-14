lst=[]
a = 0
b = 1
for i in range(9):
    result=lst.append(a)
    c = a + b
    a = b
    b = c
result=tuple(lst)
print(result)      
