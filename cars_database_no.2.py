# Import the SQLite library
import sqlite3

# Set the database to connect to
DATABASE = 'cars.db'

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Select information
cursor.execute("SELECT number_plate, driver FROM car")
results = cursor.fetchall()

# Print welcome message
print("Welcome to the cars database")

for result in results:
    print(f"{result[0]:10} {result[1]:10}")

# Get number plate to display
no_blank = True
while no_blank == True:
    selection = input("Enter number plate: ")
    selection = selection.upper()
    if selection.replace(" ", "") == "":
        print("Please enter a number plate.")
    else:
        no_blank = False
slection = "%" + selection + "%"

#Get details of selected car
cursor.execute("SELECT * FROM car WHERE number_plate LIKE ?", (slection,))
car_results = cursor.fetchall()
number_of_results = len(car_results)

#Print number of results found
if car_results == []:
    print("0 result(s) found")
else:
    print(f"{number_of_results} result(s) found")
    #Print table of results
    print("ID  Plate  Colour     Driver          Make      Model")
    print("=======================================================")
    for s in car_results:
        print(f"{s[0]:3} {s[1]:6} {s[2]:10} {s[3]:15} {s[4]:10} {s[5]:10}")


