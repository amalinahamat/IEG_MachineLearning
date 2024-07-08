from os.path import exists

def keyboard_input(datatype,caption, errorMessage, defaultValue=None):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if (value.strip() == ""):
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value


def doMenu(file):
    choice = -1
    while (choice != 0):
        print("---------------------------")
        print("|         MENU            |")
        print("| 0 -     EXIT            |")
        print("| 1 - Reporting Accident  |")
        print("| 2 - List Description    |")
        print("| 3 - Add Description     |")
       #print("| 3 - Edit Description    |")
       #print("| 4 - Delete              |")
        print("---------------------------")
        choice = keyboard_input(int, "Choice [0, 1, 2, 3]: ", "Choice must be Integer")
        if (choice == 0):
            print("Thank you for using our system")
            break
        elif (choice == 1):
            accidentReport(cars)
        elif (choice == 2):
            printDescription(file)
        elif (choice == 3):
            addDescription(file)


def createFile(file):
    if not exists(file):
        try:
            filehandler = open(file, 'xt')
        except Exception as e:
            print ("Something went wrong when we create the file:", e)
        else:
            createFile(file)
        finally:
            filehandler.close()

def createTitle(file):
    try:
        with open(file, 'wt') as filehandler:
            filehandler.write("Description | Environmental Condition | Date | Time | Status | Amount")
    except Exception as e:
        print("Something went wrong when we create the header:", e)


def addDescription(file):
    try:
        description = keyboard_input(str, "Description: ", "Description must be String.")
        environment = keyboard_input(str, "Environmental Condition: ", "Environmental Condition must be String.")
        date = keyboard_input(int, "Date: ", "Date must be integer.")
        time = keyboard_input (int, "Time: ", "Time must be integer.")
        status = keyboard_input(str, "Status: ", "Status must be String.")
        amount = keyboard_input(int, "Amount: ", "Amount must be String.")

        with open (file, "at") as filehandler:
            filehandler.write(f"\n{description} | {environment} | {date} | {time} | {status} | {amount}")
    except Exception as e:
        print("Something went wrong when we append the description:", e)
        

def printDescription(file):
    try:
        lines = None
        with open (file, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            description, environment, date, time, status, amount = line.strip().split("|")
            if (index == 0):
                print(f"{"No.":5}{description:20}{environment:>20}{date:>20}{time:>20}{status:>20}{amount:>20}")
                print("=" * 130)
            else:
                print(f"{index:<5}{description:20}{environment:>20}{int(date):>23}{int(time):>21}{str(status):>20}{int(amount):>20}")
    except Exception as e:
        print ("Something went wrong when we print the description:", e)


def accidentReport(cars):
    print (f"Checking if the file '{cars}' exists... ")
    if exists(cars):
        print (f"File '{cars}' exists. Attempting to read...")
        try:
            with open(cars, "rt") as filehandler:
                content = filehandler.read()
                print(f"Contents of '{cars}' : \n{content}")
        except Exception as e:
            print("Something went wrong when reading the cars list file!")
    else:
        print(f"File '{cars}' does not exist")      
   


# def openbooking(book):
    # try:
        # with open(book, 'rt') as filehandler:
            # lines = filehandler.readlines()
        # return lines
    # except Exception as e:
        # print("Something went wrong when we open:", e)



file = "accident.txt"
cars = "cars.txt"
#book = "booking.txt"
# createFile(file)
createTitle(file)
doMenu(file)




# For Testing function:

#addDescription(file)
#printDescription(file)
#openfile = openbooking("booking.txt")
#print (openfile)
#accidentReport(cars)