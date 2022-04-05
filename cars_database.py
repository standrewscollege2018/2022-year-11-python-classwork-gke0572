import sqlite3
DATABASE = 'cars.db'
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

cursor.execute("SELECT * FROM car WHERE colour = 'Red'")
results = cursor.fetchall()
number_of_results = len(results)
print(f"There are {number_of_results} red cars")
