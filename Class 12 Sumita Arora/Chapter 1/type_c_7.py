def find_sum(n):
    sum = 0
    if n >= 0:
        for i in range(n, 2 * n + 1):
            sum += i
        return sum    
    else:
        for i in range(2 * n, n + 1):
            sum += i
        return sum    
n = int(input("Enter a number: "))
print("Sum =", find_sum(n))