import csv 
from datetime import datetime
from actions import getToday, getWeek

ENTER_HABITS = "Please enter the list of habits, separated by commas: "
WEEK_NUMBER = "Week Number"
DAY = "Day"

# method to create a new file in the working directory with name fileName
def createFile(fileName):
    # create the headers row 
    header = [WEEK_NUMBER, DAY]
    numOfHabits = 0
    habits = input(ENTER_HABITS)
    if habits[-1] == ",":
        habits = habits[:len(habits)-1]
    habitsArr = habits.split(",")
    for habit in habitsArr:
        newHabit = habit.strip().capitalize()
        if newHabit not in header:
            header.append(newHabit)
            numOfHabits += 1

    f = open(fileName, "w")
    writer = csv.writer(f)
    writer.writerow(header)

    # create the initial row
    today = getToday()
    week = getWeek(today)
    initialRow = [week, today]
    for i in range(numOfHabits):
        initialRow.append(0)
    writer.writerow(initialRow)
    f.close()