import csv

# function to return the habits in fileName
# assumes fileName is not empty
def getHabits(fileName):
    numNoneHabits = 2
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            habits = row[numNoneHabits:]
            return habits