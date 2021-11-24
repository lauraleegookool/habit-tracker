import csv
from datetime import datetime

# function to return the habits in fileName
# assumes fileName is not empty
def getHabits(fileName):
    numNoneHabits = 2
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            habits = row[numNoneHabits:]
            return habits

# opens fileName to write to it 
# selects a given date and habit in spreadsheet to either add or overwrite an amount of data for that habit
# fileName -> file to open
# habit -> habit to know which column in file
# amount -> amount of minutes to add to date for habit
# date -> date to know which row in file, default is today's date
def addDataToFile(fileName, habit, amount, date = datetime.today().strftime("%x")):
    with open(fileName, "r") as f:
        lastLine = f.readlines()[-1]
        lastDate = lastLine.split(",")[1]
        if lastDate != date and date == datetime.today().strftime("%x"):
            # if this is true, simply add a row to the csv file
            print("TODO")
        else:
            # loop through csv and find the date. If date not found, add row with data
            # add remaining rows to csv afterwards
            print("TODO")