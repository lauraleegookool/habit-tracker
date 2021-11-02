from list import *
from readCSV import *
HELP = "help"
EXIT = "e"
ERROR = "Unrecognised input"
INVALID_FILE = "File name not found"
LIST = "ls"
CREATE = "c"
WRITE = "w"
READ = "r"
newLine = "\n"
listHelp = "To view the list of spreadsheets in the current directory, enter 'ls'"
createHelp = "To create a new spreadsheet, enter 'c <name>' where <name> is the name of the spreadsheet you want to create"
readHelp = "To read from an existing spreadsheet, enter 'r <name>' where name is the name of the spreadsheet you wish to read"
writeHelp = "To write data to an existing spreadsheet, enter 'w <name>' where name is the name of the spreadsheet you wish to add to"
def help():
    print(listHelp + newLine)
    print(createHelp + newLine)
    print(readHelp + newLine)
    print(writeHelp)

def main():
    files = []
    print("Hello, welcome to habit tracker. Please enter a command. For help, enter 'help'")
    while(True):
        cmd = input("")
        args = cmd.split(" ")
        prompt = args[0]
        if prompt == HELP:
            help()
        elif prompt == EXIT:
            break
        elif prompt == LIST:
            files = getList()
            for file in files:
                print(file)
        elif len(args) == 2:
            if prompt == CREATE:
                print("do something with creating")
            elif prompt == WRITE:
                print("do something with writing")
            elif prompt == READ:
                fileName = args[1]
                if fileName not in files:
                    print(INVALID_FILE)
                else:
                    readFile(fileName)
            else:
                print(ERROR)
        else:
            print(ERROR)

main()