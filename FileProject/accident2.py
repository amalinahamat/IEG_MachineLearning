from os.path import exists
from datetime import datetime

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


def date_input(caption, errorMessage, defaultValue=None):
    value = None
    isInvalid = True
    while isInvalid:
        try:
            value = input(caption)
            if defaultValue is not None and value.strip() == "":
                return defaultValue
            value = datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError as e:
            print(errorMessage, e)
        else:
            isInvalid = False
    return value


def time_input(caption, errorMessage, defaultValue=None):
    value = None
    isInvalid = True
    while isInvalid:
        try:
            value = input(caption)
            if defaultValue is not None and value.strip() == "":
                return defaultValue
            value = datetime.strptime(value, "%I:%M%p").time()
        except ValueError as e:
            print(errorMessage, e)
        else:
            isInvalid = False
    return value


def doMenu(file, cars, booking):
    choice = -1
    while (choice != 0):
        print("---------------------------")
        print("|         MENU            |")
        print("| 0 -     EXIT            |")
        print("| 1 - Reporting Accident  |")
        print("| 2 - Updating Report     |")
        print("| 3 - List of Report      |")
        print("| 4 - Delete Report       |")
        print("| 5 - Damage Claim        |")
        print("---------------------------")
        choice = keyboard_input(int, "Choice [0, 1, 2, 3, 4, 5]: ", "Choice must be Integer")
        if (choice == 0):
            print("Thank you for using our system")
            break
        elif (choice == 1):
            platNo, car_choice = selectCar(cars, booking)
            if platNo is not None:
                accidentReport(file, car_choice, platNo, cars, booking)
        elif (choice == 2):
            updateReport(file)
        elif (choice == 3):
            printReport(file)
        elif (choice == 4):
            deleteReport(file)
        elif(choice == 5):
            printDamageClaims(file)
        
            
def createFile(file):
    if not exists(file):
        try:
            filehandler = open(file, 'xt')
        except Exception as e:
            print ("Something went wrong when we create the file:", e)
        else:
            createTitle(file)
        finally:
            filehandler.close()


def createTitle(file):
    try:
        with open(file, 'wt') as filehandler:
            filehandler.write("Car Detail | Description | Environment Condition | Date | Time | Status | Amount")
    except Exception as e:
        print("Something went wrong when we create the header:", e)   
   

def selectCar(cars, booking):
    try:
        with open(cars, "rt") as filehandler:
            lines = filehandler.readlines()
        print("\nSelect a car from the list:")
        for index, line in enumerate(lines):
            # print(f"{index + 1}. {line.strip()}")
            platNo, modelCar, nameCar, colorCar, statusCar = line.strip().split(" | ")
            if index == 0:
                print(f"{'No.':<5}{platNo:<10}{modelCar:<10}{nameCar:<10}{colorCar:<10}{statusCar:<10}")
                print("="*80)
            else:
                print(f"{index:<5}{platNo:<10}{modelCar:<10}{nameCar:<10}{colorCar:<10}{statusCar:<10}")
                
        choice = keyboard_input(int, "\nEnter the number of the car: ", "Choice must be an integer.")
        if 0 > choice >= len(lines):
            print("Invalid choice, please select a valid car number.")
            return selectCar(cars, booking)
        else:
            # Read and display booking.txt
            selected_car = lines[choice].strip().split(" | ")[0]
            # platNo, _, _, _, _ = selected_car.strip().split(" | ")
            # selected_car = platNo
            # platNo = selected_car[1]
            # Read and display booking.txt
            with open(booking, "rt") as booking_filehandler:
                booking_lines = booking_filehandler.readlines()
            print("\nBooking Details:")
            bookingRelated = [line.strip() for line in booking_lines[0:] if line.startswith(selected_car.split()[0])]
            for booking_index, booking_line in enumerate(bookingRelated):
                print(f"{booking_index + 1}. {booking_line}")

            # platNorelated = bookingRelated[0].split(" | ")[0]
                # return platNorelated, choice
            # if bookingRelated:
            #     return selected_car, choice
            # else:
            #     print("No booking found for the selected car.")
            #     return None
            
    except Exception as e:
        print("Something went wrong when selecting a car:")
        return None


def accidentReport(file, car_choice, cars, platNorelated, booking):

    try:
        with open(booking, "rt") as booking_filehandler:
            lines = booking_filehandler.readlines()
        for line in lines:
            car_platNo, _, startRent, endRent = line.strip().split(" | ")
            # startRent = datetime.strptime(startRent, "%d/%m/%Y").date()
            # endRent = datetime.strptime(endRent, "%d/%m/%Y").date()
            # break  # Assuming the plate number is in the first line
        plateNum = keyboard_input(str, "\nCar Detail: ", "Car detail must be String.")
            # if car_platNo == platNo:
        description = keyboard_input(str, "\nDescription[Light/Medium/Extreme Accident]: ", "Description must be String.")
        environment = keyboard_input(str, "Environment Condition[Road:Bumpy/Slippery] | [\033[1mWeather\033[0m:Sunny/Rain]: ", "Environment Condition must be String.")
        date = date_input("Date (DD/MM/YYYY): ", "Date must be in DD/MM/YYYY format.")
        time = time_input("Time (12 Hour Format): ", "Time must be in 12-Hour format.")
        status = keyboard_input(str, "Status[Paid/Unpaid]: ", "Status must be String.")
        amount = keyboard_input(str, "Amount [RM]: ", "Amount must be String.")

        # matches = [date for date in lines if startRent <= date <= endRent]

        # if date in matches:
            # print(f"{line.strip().split(" | ")}")

        # with open(booking, "rt") as booking_filehandler:
        #         booking_lines = booking_filehandler.readlines()
        # bookingRelated = [line.strip() for line in booking_lines[1:] if line.startswith(selected_car.split()[0])]
        # for booking_index, booking_line in enumerate(bookingRelated):
        #     platNo, custName, startRent, endRent = booking_line.strip().split(" | ")
        


        with open(file, "at") as filehandler:
            filehandler.write(f"\n{plateNum} | {description} | {environment} | {date.strftime('%d/%m/%Y')} | {time} | {status} | {amount}")
    except Exception as e:
        print("Something went wrong when we append the accident report:", e)

    

def printReport(file):
    try:
        with open (file, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
                car_detail,description, environment, date, time, status, amount = line.strip().split(" | ")
                if (index == 0):
                    print(f"{'No.':5}{car_detail:15}{description:20}{environment:>20}{date:>15}{time:>15}{status:>20}{amount:>19}")
                    print("=" * 138)
                else:
                    print(f"{index:<5}{car_detail:15}{description:20}{environment:>15}{str(date):>25}{str(time):>15}{str(status):>20}{str(amount):>19}")
    except Exception as e:
        print ("Something went wrong when we print the description:", e)


def updateReport(file):
    try:
        with open(file, "rt") as filehandler:
            lines = filehandler.readlines()
        data = [line.strip().split(" | ") for line in lines]
        for index, line in enumerate(data[1:], start=1):
            print(f"{index}. {line}")
        index = keyboard_input(int, "Please key in the index of the Report: ", "Index must be integer")

         # Validate index
        if index < 1 or index >= len(data):
            print("Sorry, report not available")
        else:
            # Display the selected report
            report = data[index]
            car_detail,description, environment, date, time, status, amount = report
            print(f"\nReport Details:\nCar Detail: {car_detail}\nDescription: {description}\nEnvironment Condition: {environment}\nDate: {date}\nTime: {time}\nStatus: {status}\nAmount: {amount}")

            # Confirm update
            confirm = keyboard_input(str, "Are you sure you want to edit this report (y/n)? ", "Response must be string")
            if confirm.lower() == 'y':
                # Get new values or keep existing if left empty
                new_car = keyboard_input(str,f"Car [{car_detail}]: ", "Car Detail must be a String.", car_detail)
                new_description = keyboard_input(str, f"Description [{description}]: ", "Description must be String", description)
                new_environment = keyboard_input(str, f"Environment Condition [{environment}]: ", "Environment Condition must be String", environment)
                new_date = date_input(f"Date [{date}]: ", "Date must be in YYYY-MM-DD format.", date)
                new_time = time_input(f"Time [{time}]: ", "Time must be in HH:MM format.", time)
                new_status = keyboard_input(str, f"Status [{status}]: ", "Status must be String", status)
                new_amount = keyboard_input(str, f"Amount [{amount}]: ", "Amount must be String", amount)

                # Update report in the data list
                data[index] = [new_car, new_description, new_environment, new_date, new_time, new_status, new_amount]

                # Convert the data back to lines
                newlines = [" | ".join(map(str, report)) + "\n" for report in data]
                newlines[-1] = newlines[-1].strip()  # Remove newline from the last line

                # Write updated lines back to the file
                with open(file, "wt") as filehandler:
                    filehandler.writelines(newlines)
                print("Report updated successfully.")

    except Exception as e:
        print("Something went wrong when updating the report:", e)


def deleteReport(file):
    try:
        with open(file, "rt") as filehandler:
            lines = filehandler.readlines()
        print("Select a report to delete:")
        for index, line in enumerate(lines[1:], start = 1):
            print(f"{index}. {line.strip()}")
        choice = keyboard_input(int, "Enter the number of the report to delete: ", "Choice must be an integer.")
        if 1 <= choice <= len(lines) - 1:
            lines.pop(choice)  # Remove the selected report
            
            with open(file, "wt") as filehandler:
                filehandler.writelines(lines)
            print("Report deleted successfully.")
        else:
            print("Invalid choice.")
    except Exception as e:
        print("Something went wrong when deleting the report:", e)

def printDamageClaims(file):
    car_details = []
    status_ = []
    amounts = []

    try:
        with open(file, 'rt') as filehandler:
            accidentlines = filehandler.readlines()
        for line in accidentlines:
            values = line.strip().split("|")
            car_details.append(values[0])
            status_.append(values[5])
            amounts.append(values[6])

        for i, _ in enumerate(car_details):
            if i == 0:
                print(f"{"No.":5}{car_details[i]:<10}{amounts[i]:<10}{status_[i]:<11}")
                print("="*35)
            else:
                print(f"{i:<5}{car_details[i]:<10}{amounts[i]:<10}{status_[i]:<10}")
        
        statusChoice = keyboard_input(str, "Do you want to continue for payment claims? [y/n]: ", "Response must be string")
        if statusChoice == 'y':
            while statusChoice.lower() not in ['y','n']:
                statusChoice = input("Please enter y or n:")
            else:
                changeStatus(car_details, status_, amounts, file)
        
    except Exception as e:
            print("Something went wrong when print the reports:", e)
    
    return car_details,  status_, amounts


def changeStatus(car_details, status_, amounts, file):
    try:
        with open(file, "rt") as filehandler:
            lines = filehandler.readlines()
        data = [line.strip().split(" | ") for line in lines]
        # print(data)
        # for i, _ in enumerate(car_details):
        #     if i == 0:
        #         print(f"{"No.":5}{car_details[i]:<10}{amounts[i]:<10}{status_[i]:<11}")
        #         print("="*50)
        #     else:
        #         print(f"{i:<5}{car_details[i]:<10}{amounts[i]:<10}{status_[i]:<10}")

        indexChoice = keyboard_input(int, "Enter the number from the list: ", "Index must be an Integer")
        if indexChoice <= 0 or indexChoice >= len(car_details):
            print("Invalid index.")
        else: 
            # print(data[indexChoice])       
            choicePaid = keyboard_input(str, f"You want fully paid the amount [RM {amounts[indexChoice]}] for plate number [{car_details[indexChoice]}]? [y/n]: ", "Respond must be an String")
            if choicePaid.lower() == 'y':
                plat_no, description, environment, date, time, status, amount = data[indexChoice]
                if status == "unpaid":

                    # old_line = data[indexChoice]
                    # print(data[indexChoice])
                    # plat_no, description, environment, date, time, status, amount = old_line.strip().split(" | ")
                    # plat_no, description, environment, date, time, status, amount = data[indexChoice]

                    status = "paid"
                    amount = "0"
                    # new_line = f"{plat_no} | {description[indexChoice]} | {environment[indexChoice]} | {date[indexChoice]} | {time[indexChoice]} | {status[indexChoice] = "paid"} | {0"
                    data[indexChoice] = [plat_no, description, environment, date, time, status, amount]
                else:
                    print("Invalid input")
                
        newlines = []
        for i in data:
            line = " | ".join(map(str, i)) + "\n"
            newlines.append(line)
        newlines[-1] = newlines[-1].strip()
        with open(file, "wt") as filehandler:
            filehandler.writelines(newlines)
        print("Damage claims successfully updated.")
        print("Done! You have successfully paid.")
 
    except Exception as e:
        print("Something went wrong when update the report:", e)




file = "accident.txt"
cars = "cars.txt"
booking = "booking.txt"

createFile(file)
doMenu(file, cars, booking)

# selected_car, index = selectCar(file, cars)
# if selected_car:
#     accidentReport(file, selected_car, index, cars)
# car_details, dates, times, status_, amounts, custNames, startRents, endRents = combineData(file, booking)
# printCombinedData(platNos, dates, times, status_, amounts, custNames, startRents, endRents)

#For Testing function:
#createTitle(file)
#addDescription(file)
#printDescription(file)
#openfile = openbooking("booking.txt")
#print (openfile)
#accidentReport(cars)