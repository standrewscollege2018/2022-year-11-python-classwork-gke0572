'''The Tournament code'''

#Welcome the user and ask for the name of their team
print("Welcome to the Super Tournament Points Calculation system")
enter_my_team = True
while enter_my_team == True:
    my_team = input("Enter the name of your team: ")
    try:
        check_my_team = int(my_team)
        print("Please enter a valid team name.")
    except ValueError:
        if my_team == "":
            print("Please enter a valid team name.")
        else:
            enter_my_team = False

#Collect team name's of the opponents, check if it is a string and add it to a list
teams = []
print("Enter the name of your opponents (enter 'done' when finished)")
ask_opponent_name = True
while ask_opponent_name == True:
    check_opponent_name = True
    while check_opponent_name == True:
        opponent = input("Enter the name of an opponent: ")
        try:
            number_opponent_name = int(opponent)
            print("Please enter a valid team name.")
        except ValueError:
            if opponent == "":
                print("Please enter a valid team name.")
            else:
                check_opponent_name = False
    if opponent == "done":
        ask_opponent_name = False
    else:
        teams.append(opponent)

#Print and collect Results
points = []
#Sets it so it repeats for the amount of teams my team versus
for i in range(0, len(teams)):
    print(f"Game versus {teams[i]}")
    check_my_score = True
    #Enters my teams score and checks if it is a valid score
    while check_my_score == True:
        try:
            my_score = int(input(f"{my_team} score: "))
            if my_score < 0:
                print("Please enter a valid integer.")
            else:
                check_my_score = False
        except ValueError:
            print("Please enter a valid integer.")
    #Enters my opponents score and checks if it is a valid score       
    check_opponent_score = True
    while check_opponent_score == True:
        try:
            their_score = int(input(f"{teams[i]} score: "))
            if their_score < 0:
                print("Please enter a valid integer.")
            else:
                check_opponent_score = False
        except ValueError:
            print("Please enter a valid integer.")
    #Determines whether my team won, lost or drew
    if my_score > their_score:
        print("You won")
        point = 3
    elif my_score < their_score:
        print("You lost")
        point = 1
    else:
        print("You drew")
        point = 2
    #Sets the amount of points my team gets and adds it to a list
    points.append(point)

#Calculate points and print final message
total = 0
for i in range(0, len(points)):
    total = total + points[i]
print("Competition complete!")
print(f"{my_team} finished the competition with {total} points.")
