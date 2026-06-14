cricket = {
    18: "Virat Kohli",
    2: "phil salt",
    3: "rajat patidar",
    4: "bhuvneshwar kumar",
    5: "tim david"
}
value = input("Enter player name: ")
for key in cricket:
    if cricket[key].lower() == value.lower():
        print("Key =", key)
        break
else:
    print("Value not found")