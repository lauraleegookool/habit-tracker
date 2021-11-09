from list import *
from readCSV import *
from createCSV import *
from write import *
HELP = "help"
EXIT = "e"
ERROR = "Unrecognised input"
INVALID_FILE = "File name not found"
LIST = "ls"
CREATE = "c"
WRITE = "w"
READ = "r"
newLine = "\n"
listHelp = "To view the list of spreadsheets in the current directory, enter '{command}'\n"
createHelp = "To create a new spreadsheet, enter '{command} <name>' where <name> is the name of the spreadsheet you want to create\n"
readHelp = "To read from an existing spreadsheet, enter '{command} <name>' where name is the name of the spreadsheet you wish to read\n"
writeHelp = "To write data to an existing spreadsheet, enter '{command} <name>' where name is the name of the spreadsheet you wish to add to\n"
def help():
    print(listHelp.format(command = LIST))
    print(createHelp.format(command = CREATE))
    print(readHelp.format(command = READ))
    print(writeHelp.format(command = WRITE))

def main():
    files = getList()
    print("Hello, welcome to habit tracker. Please enter a command. For help, enter '{0}'. To exit, enter '{1}'".format(HELP, EXIT))
    while(True):
        cmd = input("")
        args = cmd.split(" ")
        prompt = args[0]
        if prompt == HELP:
            help()
        elif prompt == EXIT:
            break
        elif prompt == LIST:
            for file in files:
                print(file)
        elif len(args) == 2:
            fileName = args[1]
            if prompt == CREATE:
                createFile(fileName)
            elif prompt == WRITE:
                writeToFile(fileName)
            elif prompt == READ:
                if fileName not in files:
                    print(INVALID_FILE)
                else:
                    readFile(fileName)
            else:
                print(ERROR)
        else:
            print(ERROR)

main()