'''Rental Cars'''
#Create list with cars
cars = [["Suzuki Van", "(2)", False],
        ["Toyota Corolla", "(4)", False],
        ["Honda CRV", "(4)", False],
        ["Suzuki Swift", "(4)", False],
        ["Mitsubishi Airtreck", "(4)", False],
        ["Nissan DC Ute", "(4)", False],
        ["Toyota Previa", "(7)", False],
        ["Toyota Hi Ace", "(12)", False],
        ["Toyota Hi Ace", "(12)", False]]

#Introduce the program and display vehicles for hire
print("Welcome to the University vehicle rental system.")
print("The vehicles are:")
for i in range(0, len(cars)):
    if cars[i][2] == True:
        print(f"{i+1}.{cars[i][0]} {cars[i][1]} - Unavailable")  
    else:
        print(f"{i+1}. {cars[i][0]} {cars[i][1]}")
number_vehicle = int(input("Which vehicle would you like to book? "))
