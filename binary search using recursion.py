def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)
a = input("Enter space separated arrays: ")
a = [int(i) for i in a.split()]
print(a)
target = int(input("Enter target: "))
result = binary_search(a, target, 0, len(a) - 1)
if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)