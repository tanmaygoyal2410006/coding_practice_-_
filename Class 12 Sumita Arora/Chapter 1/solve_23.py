total = 0
while True:
    num = input("Enter a number (or done): ")
    if num == "done":
        break
    total = total + int(num)
print("Sum =", total)
