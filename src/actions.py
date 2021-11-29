import csv
from datetime import datetime

WEEK_INDEX = 0
DAY_INDEX = 1
HABITS_INDEX = 2

# checks that the format of date is valid
def checkDateFormat(date):
    length = len(date)
    if length != 10:
        return False
    items = date.split("-")
    if len(items) != 3:
        return False
    if len(items[0]) != 4:
        return False
    if len(items[1]) != 2:
        return False
    if len(items[2]) != 2:
        return False
    if int(items[1]) not in range(1, 13):
        return False
    if int(items[2]) not in range(1, 32):
        return False
    return True

# function to return the habits in fileName
# assumes fileName is not empty
def getHabits(fileName):
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            habits = row[HABITS_INDEX:]
            return habits

# returns the date of today in the format YYYY/MM/DD
# eg. getToday() -> "2021-11-23"
def getToday():
    today = datetime.now()
    date = str(today).split()[0]
    return date

# returns the week number in year of date 
# first day of week is monday
def getWeek(date):
    date = getDatetime(date)
    week = date.strftime("%W")
    return week

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
            day = r[DAY_INDEX]
            date = (getDatetime(day))
            if date == dateObject:
                dateRow = r
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
    habitIndex = habits.index(habit) + HABITS_INDEX
    amountToAdd = amount
    with open(fileName, "r") as f:
        lastLine = f.readlines()[-1]
        lastDate = lastLine.split(",")[1]
        if lastDate != date and date == getToday():
            # if this is true, simply add a row to the csv file
            appendRow = True
    
    if appendRow:
        with open(fileName, 'a') as f:
            writer = csv.writer(f)
            # append week and date to row 
            row = [date, date]
            for i in habits:
                row.append(0)
            row[habitIndex] = amountToAdd
            writer.writerow(row)
    else:
        rowDict = findDateInFile(fileName, date)
        beforeRow = rowDict["beforeDate"]
        afterRow = rowDict["afterDate"]
        rowDate = rowDict["dateRow"]
        if len(rowDate) > 0:
            # if this row exists, overwrite/write data 
            oldAmount = int(rowDate[habitIndex])
            rowDate[habitIndex] = oldAmount + int(amount)
        else:
            # create a new row
            weekDate = getWeek(date)
            rowDate = [weekDate, date]
            for i in habits:
                rowDate.append(0)
            rowDate[habitIndex] = amount
        with open(fileName, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(beforeRow)
            writer.writerow(rowDate)
            writer.writerows(afterRow)

# loops through data and gets the average for each habit in habits
# returns a dictionary where the key is habit and the value is the average
def getHabitAverage(data, habits, allHabits, count):
    habitAvg = {}
    for habit in habits:
        key = habit
        index = allHabits.index(habit) + HABITS_INDEX
        total = 0
        for r in data:
            amt = int(r[index])
            total += amt 
        avg = total//count
        habitAvg[key] = avg
    return habitAvg

# gets the average for a given list of habits in csv file over a range of dates 
# if dates not specified, calculates over all the dates in spreadsheet
# if only startDate given, calculates for the week that the date is in
# fileName -> file to extract data from
# habits -> a list of habits in spreadsheet
# startDate / endDate -> dates for start and end of the averages 
# returns a dictionary with the average for each habit
def getAverages(fileName, habits, startDate = None, endDate = None):
    avgRows = []
    habitAvg = {}
    if not startDate and not endDate:
        # get all averages
        with open(fileName, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for r in reader:
                avgRows.append(r)
        count = len(avgRows)
    elif startDate and not endDate:
        # get averages for a week
        weekDate = getWeek(startDate)
        with open(fileName, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            avgRows = []
            count = 7
            for r in reader:
                week = r[WEEK_INDEX]
                if week == weekDate:
                    avgRows.append(r)
    else:
        # startDate and endDate both exist
        start = getDatetime(startDate)
        end = getDatetime(endDate)
        count = (end - start).days + 1
        with open(fileName, "r") as file:
            reader = csv.reader(file)
            next(reader)
            avgRows = []
            for r in reader:
                day = getDatetime(r[DAY_INDEX])
                if day >= start and day <= end:
                    avgRows.append(r)
    allHabits = getHabits(fileName)
    habitAvg = getHabitAverage(avgRows, habits, allHabits, count)
    return (habitAvg)
