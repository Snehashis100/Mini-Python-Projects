def showDate():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d [%H:%M]")


def retrieveData(file_name):
    with open(file_name) as f:
        content = f.read()
        if len(content) == 0:
           print("*****empty*****")
        else:
           print(content)
        f.close()


def insertData(file_name, foody, stamp):
    with open(file_name, "a") as f:
        f.write(f"{stamp}: {foody}\n")
        print("Data inserted successfully")
        f.close()


if __name__ == '__main__':
    user = int(
        input("Welcome to Health Management System\nEnter 1 : For Rohan\nEnter 2 : For Harry\nEnter 3 : For Manoj\n"))
    if user == 1:
        print("Hi Rohan\n")
        user_2 = int(input("Enter 1 : For Diet\nEnter 2 : For Exercise\n"))
        if user_2 == 1:
            user_3 = int(input("Enter 1 : To retrieve data\nEnter 2 : To insert data\n"))
            if user_3 == 1:
                retrieveData("rohan_diet.txt")
            elif user_3 == 2:
                time_stamp = showDate()
                food = input("Enter the food you ate")
                insertData("rohan_diet.txt", food, time_stamp)
            else:
                print("Wrong Input")

        elif user_2 == 2:
            user_3 = int(input("Enter 1 : To retrieve data\nEnter 2 : To insert data\n"))
            if user_3 == 1:
                retrieveData("rohan_exercise.txt")
            elif user_3 == 2:
                time_stamp = showDate()
                exercise = input("Enter the name of the exercise")
                insertData("rohan_exercise.txt", exercise, time_stamp)
            else:
                print("Wrong Input")

        else:
            print("Wrong Input")

    elif user == 2:
        print("Hi Harry\n")
        user_2 = int(input("Enter 1 : For Diet\nEnter 2 : For Exercise\n"))
        if user_2 == 1:
            user_3 = int(input("Enter 1 : To retrieve data\nEnter 2 : To insert data\n"))
            if user_3 == 1:
                retrieveData("harry_diet.txt")
            elif user_3 == 2:
                time_stamp = showDate()
                food = input("Enter the food you ate")
                insertData("harry_diet.txt", food, time_stamp)
            else:
                print("Wrong Input")

        elif user_2 == 2:
            user_3 = int(input("Enter 1 : To retrieve data\nEnter 2 : To insert data\n"))
            if user_3 == 1:
                retrieveData("harry_exercise.txt")
            elif user_3 == 2:
                time_stamp = showDate()
                exercise = input("Enter the name of the exercise")
                insertData("harry_exercise.txt", exercise, time_stamp)
            else:
                print("Wrong Input")

        else:
            print("Wrong Input")

    elif user == 3:
        print("Hi Manoj\n")
        user_2 = int(input("Enter 1 : For Diet\nEnter 2 : For Exercise\n"))
        if user_2 == 1:
            user_3 = int(input("Enter 1 : To retrieve data\nEnter 2 : To insert data\n"))
            if user_3 == 1:
                retrieveData("manoj_diet.txt")
            elif user_3 == 2:
                time_stamp = showDate()
                food = input("Enter the food you ate")
                insertData("manoj_diet.txt", food, time_stamp)
            else:
                print("Wrong Input")

        elif user_2 == 2:
            user_3 = int(input("Enter 1 : To retrieve data\nEnter 2 : To insert data\n"))
            if user_3 == 1:
                retrieveData("manoj_exercise.txt")
            elif user_3 == 2:
                time_stamp = showDate()
                exercise = input("Enter the name of the exercise")
                insertData("manoj_exercise.txt", exercise, time_stamp)
            else:
                print("Wrong Input")

        else:
            print("Wrong Input")

    else:
        print("Wrong Input")
