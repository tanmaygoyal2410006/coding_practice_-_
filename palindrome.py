
def check_palindrome(name):
    i = 0
    j = len(name) - 1
    while(i < j):
        if(name[i] != name[j]):
            return False
        i += 1
        j -= 1
    return True
name=input("enter your name: ")
print(name, " is palindrome.") if check_palindrome(name) else print(name, " is not palindrome.")

    