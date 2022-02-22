#health management system
#3 client- rohan, harry, hammad
# total 6 files
#write a function that when executed takes as input client name
#one more function to retreve exercise or food for any client

# client_name = {"Harry":"1",
#                "Rohan":"2",
#                "hammad":"3"}
# data = {"Exercise":"1",
#         "Diet":"2"}
# Action = {"Add data":"1",
#           "Read data":"2"}
def getdate():
    import datetime
    return datetime.datetime.now()
date_and_time = getdate()
date = str(date_and_time)

print("What action do you want to perform\nAdd to existing Data\tRead from existing Data\npress 1\t\t\t\t\tpress 2")
action = int(input("Enter your answer here: "))

# def dataentry(client_name,data):
#     if data == "Diet":
#         client_name_diet = open("client_name Diet plan", "a")
#         client_name_diet = str(input("Enter what did he eat now:"))
#         client_name_diet.write(date)
#         client_name_diet.write(client_name_diet)
#         client_name_diet.close()
#
#     elif data == "Exercise":
#         harry_exercise = open("Harry's Exercise plan", "a")
#         His_exercise = str(input("Enter what did he do now:"))
#         harry_exercise.write(date)
#         harry_exercise.write(His_exercise)
#         harry_exercise.close()
#     else:
#         print("Select appropiate value and try again.")
#

if action == 1:

    print("Which client are you looking for { Harry , Rohan , Hamad }")
    client_name = str(input("Enter client name here: "))
    if client_name == "Harry":
        print("What you want to update Diet or Exercise")
        data = str(input("Type your response here: "))
        if data == "Diet":
            harry_diet = open("Harry's Diet plan","a")
            His_diet = str(input("Enter what did he eat now:"))
            harry_diet.write(date)
            harry_diet.write(His_diet)
            harry_diet.close()

        elif data == "Exercise":
            harry_exercise = open("Harry's Exercise plan", "a")
            His_exercise = str(input("Enter what did he do now:"))
            harry_exercise.write(date)
            harry_exercise.write(His_exercise)
            harry_exercise.close()
        else:
            print("Select appropiate value and try again.")

    elif client_name == "Rohan":
        print("What you want to update Diet or Exercise")
        data = str(input("Type your response here: "))
        if data == "Diet":
            rohan_diet = open("Rohan's Diet plan", "a")
            His_diet = str(input("Enter what did he eat now:"))
            rohan_diet.write(date)
            rohan_diet.write(His_diet)
            rohan_diet.close()

        elif data == "Exercise":
            rohan_exercise = open("Rohan's Exercise plan", "a")
            His_exercise = str(input("Enter what did he do now:"))
            rohan_exercise.write(date)
            rohan_exercise.write(His_exercise)
            rohan_exercise.close()
        else:
            print("Select appropiate value and try again.")

    elif client_name == "Hamad":
        print("What you want to update Diet or Exercise")
        data = str(input("Type your response here: "))
        if data == "Diet":
            hamad_diet = open("Hamad's Diet plan", "a")
            His_diet = str(input("Enter what did he eat now:"))
            hamad_diet.write(date)
            hamad_diet.write(His_diet)
            hamad_diet.close()

        elif data == "Exercise":
            hamad_exercise = open("Hamad's Exercise plan", "a")
            His_exercise = str(input("Enter what did he do now:"))
            hamad_exercise.write(date)
            hamad_exercise.write(His_exercise)
            hamad_exercise.close()
        else:
            print("Select appropiate value and try again.")

    else:
        print("Name not in the data base")


elif action == 2:
    print("Who's data do you want to see{ Harry , Rohan , Hamad }")
    client_name = str(input("Enter client name here: "))
    if client_name == "Harry":
        data = str(input("What data do you want Diet or Exercise: "))
        if data == "Diet":
            harry_diet = open("Harry's Diet plan", "rt")
            print(harry_diet.readlines())
        elif data == "Exercise":
            harry_exercise = open("Harry's Exercise plan", "rt")
            print(harry_exercise.readlines())
        else:
            print("Invalid data")
    elif client_name == "Rohan":
        data = str(input("What data do you want Diet or Exercise: "))
        if data == "Diet":
            rohan_diet = open("Rohan's Diet plan", "rt")
            print(rohan_diet.readlines())
        elif data == "Exercise":
            rohan_exercise = open("Rohan's Exercise plan", "rt")
            print(rohan_exercise.readlines())
        else:
            print("Invalid data")

    elif client_name == "Hamad":
        data = str(input("What data do you want Diet or Exercise: "))
        if data == "Diet":
            hamad_diet = open("Hamad's Diet plan", "rt")
            print(hamad_diet.readlines())
        elif data == "Exercise":
            hamad_exercise = open("Hamad's Exercise plan", "rt")
            print(hamad_exercise.readlines())
        else:
            print("Invalid data")
    else:
        print("Name not in data base")


else:
    print("Select a proper number")


