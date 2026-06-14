def duplicate(l):
    for i in l:
        if l.count(i) > 1:
            return True
    return False    
lst = list(input("Enter elements of list "))
print(duplicate(lst))

# Do it with nlogn complezity, read and implement set, also implement it with sort.
