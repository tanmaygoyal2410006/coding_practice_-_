sentence=input("enter a sentence: ")
words=len(sentence.split())
characters=len(sentence)
alpha_num=0
for i in sentence:
    if i.isalnum():
        alpha_num+=1
percent_alpha_num=(alpha_num/characters)*100
print("number of words: ",words)
print("number of characters: ",characters)
print("percentage of alphanumeric characters: ",percent_alpha_num)        