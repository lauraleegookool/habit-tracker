from actions import getAverages, getHabits

def getPrompts():
    # COMMANDS
    all_avgs = "avg a"
    all_avgs_in_range = "avg a <startDate> <endDate>"
    habit_avg_in_range = "avg <habit> <startDate> <endDate>"
    all_avgs_in_week = "avg a w <weekDate>"
    habit_avg_in_week = "avg <habit> w <weekDate>"
    formatting = "YYYY-MM-DD"
    # PROMPTS
    all_avgs_prompt = "To get averages for all habits in spreadsheet, enter {prompt}\n"
    all_avgs_in_range_prompt = "To get averages for all habits in a date range, enter {prompt}\n"
    habit_avg_in_range_prompt = "To get the average for a specific habit over a range of dates, enter {prompt}\n"
    all_avgs_in_week_prompt = "To get averages for all habits in a given week, enter {prompt}\n"
    habit_avg_in_week_prompt = "To get the average for a habit in a given week, enter {prompt}\n"
    formatting_prompt = "Dates are formatted as {prompt}\n"

    print(all_avgs_prompt.format(prompt=all_avgs))
    print(all_avgs_in_range_prompt.format(prompt=all_avgs_in_range))
    print(habit_avg_in_range_prompt.format(prompt=habit_avg_in_range))
    print(all_avgs_in_week_prompt.format(prompt=all_avgs_in_week))
    print(habit_avg_in_week_prompt.format(prompt=habit_avg_in_week))
    print(formatting_prompt.format(prompt = formatting))

# function to open the file fileName and producing summaries of the data in the file
def readFile(fileName):
    habits = getHabits(fileName)
    getPrompts()
    while(True):
        userInput = input("Please enter a command: \n")
        if userInput == "e":
            break
        if userInput == "h":
            getPrompts()

        args = userInput.split()
        if len(args) == 2:
            # get average over all habits for all dates
            avgs = getAverages(fileName, habits)
            keys = list(avgs.keys())
            vals = list(avgs.values())
            i = 0
            for k in keys:
                val = vals[i]
                print("{0}: {1}".format(k, val))
                i += 1
        elif len(args) == 4:
            print("TODO")
        else:
            print("Invalid format")
    