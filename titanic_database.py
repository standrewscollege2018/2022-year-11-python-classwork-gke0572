#import the sqlite library
import sqlite3

#Connect to the titanic databse
DATABASE = 'titanic.db'
connection = sqlite3.connect(DATABASE)
#Set up the sursor (so we can run queries)
cursor = connection.cursor()

ask = True
while ask == True:
    #Ask what class and check that inputs arent blank or string
    check_status = True
    while check_status == True:
        try:
            status = int(input("What class do you want to search on (1-3)? "))
            if status == "":
                print("Please enter a number between 1-3")
            elif status > 3:
                print("Please enter a number between 1-3")
            elif status < 1:
                print("Please enter a number between 1-3")
            else:
                check_status = False
        except ValueError:
            print("Please enter a number between 1-3")

    #Ask whether we want dead or alive list and check that inputs aren't blank or string
    check_survived = True
    while check_survived == True:
        try:
            survived = int(input("Enter 1 for list of survivors or 0 for deceased: "))
            if survived == "":
                print("Please enter 1 or 0")
            elif survived > 1:
                print("Please enter 1 or 0")
            elif survived < 0:
                print("Please enter 1 or 0")
            else:
                check_survived = False
        except ValueError:
            print("Please enter 1 or 0")

    #Select the names of the people who meet the inputted criteria
    cursor.execute("SELECT name FROM titanic WHERE class = ? AND survived = ?", (status, survived))
    results = cursor.fetchall()

    #Get the number of results and prints how many there are
    number_of_results = len(results)
    print(f"There are {number_of_results} results found")

    #Print the names
    for s in results:
        print(s[0])

    
    #Ask whether user wants to quit and check that inputs arent blank or input
    check_quit = True
    
    while check_quit == True:
        not_quit = input("Do you want to quit? ")
        not_quit = not_quit.lower()
        if not_quit == "":
            print("Please enter yes or no")
        elif not_quit != "yes" and not_quit != "no":
            print("Please enter yes or no.")
        else:
            check_quit = False
    if not_quit == "yes":
        ask = False
        
    

