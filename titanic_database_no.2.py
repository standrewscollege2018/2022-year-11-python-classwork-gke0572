#import the sqlite library
import sqlite3

#Connect to the titanic databse
DATABASE = 'titanic.db'
connection = sqlite3.connect(DATABASE)
#Set up the sursor (so we can run queries)
cursor = connection.cursor()

#Print welcome message
print("Welcome to the Titanic passengers database")
print("==========================================")
print("Here you can search for passengers and their details.")

#Input search and find results
print("")
search = input("Enter the name: ")
search_two = search.title()
search = "%" + search + "%"
search_two = "%" + search_two + "%"
cursor.execute("SELECT name, class, age, fare, survived FROM titanic WHERE name LIKE ? OR name LIKE ?", (search, search_two))
results = cursor.fetchall()

#Print number of results
number_of_results = len(results)
print(f"{number_of_results} result(s) found")
print("")

print("Name" + " " * 46 + "Class Age  Fare     Survived")
print("=" * 80)

for s in results:
    if s[4] == 0:
        print(f"{s[0]:49} {s[1]:5} {s[2]:4} {s[3]:8} Deceased")
    else:
        print(f"{s[0]:49} {s[1]:5} {s[2]:4} {s[3]:8} Survived")
