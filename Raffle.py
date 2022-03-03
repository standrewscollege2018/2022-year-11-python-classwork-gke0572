# Import Random package to randomly select a winner
import random

# Welcome and get prize
print("Welcome to the raffle program.")
v = True
while v == True:
    prize = input("What is the prize being raffled? ")
    if prize == "":
        print("Please enter a prize")
    else:
        v = False
    
# Ask for price and check if it is an integer
b = True
while b == True:
    try:
        price = int(input(f"What is the value of the {prize} (do not enter the $ sign) "))
    except ValueError:
        print("Please enter an integer (do not enter the $ sign)")
    else:
        b = False

# Create list that will contain the names and set ask variable
names = []
ask = True

# Ask for the name of the entrant until end is entered and add the names to the list
while ask == True:
    name = input("Enter name of entrant: ")
    if name == "":
        print("Pleases enter a name")
    else:
        if name == "end":
            ask = False
        else:
            names.append(name)

# Print the number of entrants and the prize to be won
print(f"There are {len(names)} in the draw for the {prize}.")

# Select a random number that will be the entrant in the list and print the winner
number = random.randint(0, len(names))
number -= 1

if len(names) == 0:
    print("There are no winners")
elif len(names) == 1:
    print(f"And the winner of the {prize}, valued at ${price}, is...... {names[0]}!")
else:
    print(f"And the winner of the {prize}, valued at ${price}, is...... {names[number]}!")

