def binary_search(arr, target):
    low = 0
    high=len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
            high = high
        else:
            low = low
            high = mid - 1
    return -1

# Enter main program;
a = input("Enter space separated arrays")
a = [int(i) for i in a.split()]
print(a)
target = int(input("Enter target"))
result = binary_search(a,target)
# print(result)

if(result == -1):
    print(target," not found")
else:
    print(target," found at index ",result)
           
            

