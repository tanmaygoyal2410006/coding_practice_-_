line=input("Enter a line ")
uppercase_count=0
lowercase_count=0
alphabet_count=0
digit_count=0
for i in line:
    if i.isupper():
        uppercase_count+=1
    elif i.islower():
        lowercase_count+=1
    elif i.isalpha():
        alphabet_count+=1
    elif i.isdigit():
        digit_count+=1

print("Number of Uppercase letters: ", uppercase_count)
print("Number of Lowercase letters: ", lowercase_count)
print("Number of Alphabets: ", alphabet_count)
print("Number of Digits: ", digit_count)      