
import glob
# function to return a list of .csv files in the current directory
def getList():
    files = glob.glob("*.csv")
    return files
