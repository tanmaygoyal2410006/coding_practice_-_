def merge(lst1, lst2):
    lst3 = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            lst3.append(lst1[i])
            i += 1
        else:
            lst3.append(lst2[j])
            j += 1
    while i < len(lst1):
        lst3.append(lst1[i])
        i += 1
    while j < len(lst2):
        lst3.append(lst2[j])
        j += 1

    return lst3
lst1 = [1, 2, 9, 10]
lst2 = [3, 4, 11, 12]
print(merge(lst1, lst2))