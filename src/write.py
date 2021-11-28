from actions import getHabits, addDataToFile, checkDateFormat

INVALID_FORMAT = "Invalid format\n"
HABIT_NOT_FOUND = "Habit not found. Habits are {0}"
FORMAT = "YYYY-MM-DD"

# method to add data to the specified fileName
def writeToFile(fileName):
    habits = getHabits(fileName)
    prompt = "Please enter a habit you would like to add data to.\nHabits are: {habits}.\nFormat for prompt: <date> <habit> <amount>, where:\n<date> is optional\n{dateformat}, <amount? adds to current amount in spreadsheet\n"
    while(True):
        userInput = input(prompt.format(habits = habits, dateformat = FORMAT))
        if userInput == "e":
            break
        args = userInput.split(" ")
        num = len(args)
        date, habit, amount = "", "", ""
        if num == 2:
            habit = args[0]
            amount = args[1]
            if habit not in habits:
                print(HABIT_NOT_FOUND.format(habits))
            else:
                addDataToFile(fileName, habit, amount)
        elif num == 3:
            date = args[0]
            habit = args[1]
            amount = args[2]
            if habit not in habits:
                print(HABIT_NOT_FOUND.format(habits))
            elif not checkDateFormat(date):
                print(INVALID_FORMAT)
            else:
                addDataToFile(fileName, habit, amount, date)
        else:
            print(INVALID_FORMAT)