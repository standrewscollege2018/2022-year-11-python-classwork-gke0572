'''Rental Cars'''
#Create list with cars
cars = [["Suzuki Van", "(2)", False, ""],
        ["Toyota Corolla", "(4)", False, ""],
        ["Honda CRV", "(4)", False, ""],
        ["Suzuki Swift", "(4)", False, ""],
        ["Mitsubishi Airtreck", "(4)", False, ""],
        ["Nissan DC Ute", "(4)", False, ""],
        ["Toyota Previa", "(7)", False, ""],
        ["Toyota Hi Ace", "(12)", False, ""],
        ["Toyota Hi Ace", "(12)", False, ""]]

main_loop = True
while main_loop == True:
    #Introduce the program and display vehicles for hire
    print("Welcome to the University vehicle rental system.")
    print("The vehicles are:")
    for i in range(0, len(cars)):
        if cars[i][2] == True:
            print(f"{i+1}. {cars[i][0]} {cars[i][1]} - Unavailable")  
        else:
            print(f"{i+1}. {cars[i][0]} {cars[i][1]}")

    #Choose a vehicle to book and checks that it is valid
    check_number_vehicle = True
    while check_number_vehicle == True:
        try:
            number_vehicle = int(input("Which vehicle would you like to book? "))
            if number_vehicle == 0:
                main_loop = False
                check_number_vehicle = False
            elif cars[number_vehicle - 1][2] == True:
                print("** This vehicle is already booked. Please choose another.**")
                check_number_vehicle = False
            else:
                if number_vehicle >= 10:
                    print("Please enter the number of the car you would like to rent.")
                elif number_vehicle < 0:
                    print("Please enter a valid integer.")
                else:
                    #Prints a message as too which vehicle was booked
                    number_vehicle = number_vehicle - 1
                    cars[number_vehicle][2] = True
                    print(f"You have booked the {cars[number_vehicle][0]}.")

                    #Asks for name and adds too list, thanks name
                    check_name = True
                    while check_name == True:
                        name = input("What is your name? ")
                        if name.isdigit():
                            print("Please enter a valid name.")
                        elif name.replace(" ", "") == "":
                            print("Please enter a valid name.")
                        else:
                            check_characters = False
                            for character in name:
                                if character.isalpha() == False:
                                    print("Please enter a valid name.")
                                    check_characters = True
                                    break
                                else:
                                    pass
                        if check_characters == False:
                            check_name = False
                        else:
                            pass
                    cars[number_vehicle][3] = name
                    print(f"Thanks {name}")
                    check_number_vehicle = False
        except ValueError:
                print("Please enter a valid integer.")
       
#Print Daily Summary
print("Daily Summary")
for v in range(0, len(cars)):
    if cars[v][2] == True:
        print(f"{cars[v][0]} - {cars[v][3]}")
        cars[v][2] = False
        cars[v][3] = ""
    else:
        pass
        
