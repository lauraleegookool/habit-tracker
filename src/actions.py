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

# returns the date of today in the format YYYY/MM/DD
# eg. getToday() -> "2021-11-23"
def getToday():
    today = datetime.now()
    date = str(today).split()[0]
    return date

# returns a datetime object with given date 
# requires date to be in the format "YYYY/MM/DD"
def getDatetime(date):
    dates = date.split("-")
    year = int(dates[0])
    month = int(dates[1])
    day = int(dates[2])
    dateObject = datetime(year, month, day)
    return dateObject


# searches file (fileName) for the row with date as date
# returns a dictionary with key and value pairs for rows before the given date,
# rows after the given date and the row with date itself
def findDateInFile(fileName, date):
    beforeDate = []
    afterDate = []
    dateRow = []
    dateObject = getDatetime(date)
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        beforeDate.append(header)
        for r in reader:
            day = r[1]
            date = (getDatetime(day))
            if date == dateObject:
                dateRow.append(r)
            if date < dateObject:
                beforeDate.append(r)
            if date > dateObject:
                afterDate.append(r)
    dateDict = {
        "beforeDate": beforeDate,
        "afterDate": afterDate,
        "dateRow": dateRow
    }
    return dateDict

# opens fileName to write to it 
# selects a given date and habit in spreadsheet to either add or overwrite an amount of data for that habit
# fileName -> file to open
# habit -> habit to know which column in file
# amount -> amount of minutes to add to date for habit
# date -> date to know which row in file, default is today's date
def addDataToFile(fileName, habit, amount, date = getToday()):
    appendRow = False
    habits = getHabits(fileName)
    habitIndex = habits.index(habit) + 2
    amountToAdd = amount
    with open(fileName, "r") as f:
        lastLine = f.readlines()[-1]
        lastDate = lastLine.split(",")[1]
        if lastDate != date and date == getToday():
            # if this is true, simply add a row to the csv file
            appendRow = True
        else:
            # loop through csv and find the date. If date not found, add row with data
            # add remaining rows to csv afterwards
            print("TODO")
    
    if appendRow:
        with open(fileName, 'a') as f:
            writer = csv.writer(f)
            # append week and date to row 
            row = [date, date]
            for i in habits:
                row.append(0)
            row[habitIndex] = amountToAdd
            writer.writerow(row)
