cricket = {
    18: "Virat Kohli",
    2: "phil salt",
    3: "rajat patidar",
    4: "bhuvneshwar kumar",
    5: "tim david"
}
value = input("Enter player name: ")
for i in cricket:
    if cricket[i] == value:
        print("Key =", i)
        break
else:
        print("Value not found")
