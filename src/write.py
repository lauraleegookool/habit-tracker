from datetime import datetime
# method to add data to the specified fileName
def writeToFile(fileName):
    habits = ["reading"]
    prompt = "Please enter a habit you would like to add data to.\nHabits are: {habits}.\nFormat for prompt: a <date> <habit> <+><amount>, where:\n<date> is optional\nMM/DD/YY, <+> adds to current amount in spreadsheet\n<amount> is in minutes\nIf <+> omitted, the current amount will be overwritten\n"
    while(True):
        userInput = input(prompt.format(habits = habits))
        if userInput == "e":
            break
        args = userInput.split(" ")
        num = len(args)
        date = ""
        habit = ""
        amount = ""
        if num == 2:
            # no date entered
            date = datetime.now().strftime("%x")
            habit = args[0]
            amount = args[1]
        elif num == 3:
            # date is entered. need to extract the row of data with date <date>
            date = args[0]
            habit = args[1]
            amount = args[2]
        else:
            print("Invalid format")