def get_feet():
    feet = int(input("Enter number of feet: "))
    return feet

def feet_to_inches(feet):
    return feet * 12

def display_inches(inches):
    print("Number of inches =", inches)

feet = get_feet()
inches = feet_to_inches(feet)
display_inches(inches)