from os.path import exists
from datetime import datetime

# Function to handle generic keyboard input with validation
def keyboard_input(datatype,caption, errorMessage, defaultValue=None):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            # Check for default value
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

# Function to handle date input with validation
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

# Function to handle time input with validation
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

# Main menu function
def doMenu(file, cars, booking):
    choice = -1
    while (choice != 0):
        print("---------------------------")
        print("|         MENU            |")
        print("| 0 -     EXIT            |")
        print("| 1 - Reporting Accident  |")
        print("| 2 - List of Report      |")
        print("| 3 - Delete Report       |")
        print("| 4 - Damage Claim        |")
        print("---------------------------")
        choice = keyboard_input(int, "Choice [0, 1, 2, 3, 4]: ", "Choice must be Integer")
        if (choice == 0):
            print("Thank you for using our system")
            break
        elif (choice == 1):
            selectCar(cars,booking,file)
        elif (choice == 2):
            printReport(file)
        elif (choice == 3):
            deleteReport(file)
        elif (choice == 4):
            printDamageClaims(file)
        
# Function to create a file if it doesn't exist            
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

# Function to create the title/header in the file
def createTitle(file):
    try:
        with open(file, 'wt') as filehandler:
            filehandler.write("Car Detail | Description | Environment Condition | Date | Time | Status | Amount")
    except Exception as e:
        print("Something went wrong when we create the header:", e)   

def filter_cars(lines, status_filter):
    filtered_lines = []
    for index, line in enumerate(lines):
        if index == 0:
            filtered_lines.append(line)
        else:
            platNo, modelCar, nameCar, colorCar, statusCar = line.strip().split(" | ")
            if status_filter == "a" and statusCar.lower() == "active":
                filtered_lines.append(line)
            elif status_filter == "i" and statusCar.lower() == "inactive":
                filtered_lines.append(line)
            elif status_filter == "o":
                filtered_lines.append(line)
    return filtered_lines

# Function to select a car from the list
def selectCar(cars, booking, file):
    try:
        with open(cars, "rt") as filehandler:
            lines = filehandler.readlines()

        while True:
            status_choice = keyboard_input(str, "Do you want to show active (a), inactive (i), or all cars (o)? ", "Response must be a single character (a, i, o)")
            if status_choice.lower() in ["a", "i", "o"]:
                break
            else:
                print("Invalid input, please try again.")

        filtered_lines = filter_cars(lines, status_choice.lower())

        print("\nSelect a car from the list:")
        for index, line in enumerate(filtered_lines):
            platNo, modelCar, nameCar, colorCar, statusCar = line.strip().split(" | ")
            if index == 0:
                print(f"{'No.':<5}{platNo:<10}{modelCar:<10}{nameCar:<10}{colorCar:<10}{statusCar:<10}")
                print("="*80)
            else:
                print(f"{index:<5}{platNo:<10}{modelCar:<10}{nameCar:<10}{colorCar:<10}{statusCar:<10}")

        choice = keyboard_input(int, "\nEnter the number of the car: ", "Choice must be an integer.")
        if choice < 1 or choice >= len(filtered_lines):
            print("Invalid choice, please select a valid car number.")
            return selectCar(cars, booking, file)
        else:
            # Read and display booking.txt
            selected_car = filtered_lines[choice].strip().split(" | ")[0]

            with open(booking, "rt") as booking_filehandler:
                booking_lines = booking_filehandler.readlines()
            print("\nBooking Details:")
            bookingRelated = [line.strip() for line in booking_lines if line.startswith(selected_car)]
            for booking_index, booking_line in enumerate(bookingRelated):
                print(f"{booking_index + 1}. {booking_line}")

            if bookingRelated:
                booking_choice = keyboard_input(int, "\nEnter the number of the booking: ", "Choice must be an integer.")
                if booking_choice < 1 or booking_choice > len(bookingRelated):
                    print("Invalid choice, please select a valid booking number.")
                else:
                    selected_booking = bookingRelated[booking_choice - 1]
                    accidentReport(file, selected_car, selected_booking)        
            else:
                print("No booking found for the selected car.")
                return None
                        
    except Exception as e:
        print("Something went wrong when selecting a car:", e)
        return None
    
# Function to create an accident report
def accidentReport(file, car_choice, selected_booking):

    try:

        car_platNo, _, startRent, endRent = selected_booking.split(" | ")

        plateNum = car_platNo
        description = keyboard_input(str, "\nDescription[Light/Medium/Extreme Accident]: ", "Description must be String.")
        environment = keyboard_input(str, "Environment Condition[Road:Bumpy/Slippery] | [Weather:Sunny/Rain]: ", "Environment Condition must be String.")
        date = date_input("Date (DD/MM/YYYY): ", "Date must be in DD/MM/YYYY format.")
        time = time_input("Time (9:35pm): ", "Time must be in 12-Hour format.")
        status = keyboard_input(str, "Status[Paid/Unpaid]: ", "Status must be String.")
        amount = keyboard_input(str, "Amount [RM]: ", "Amount must be String.")

        with open(file, "at") as filehandler:
            filehandler.write(f"\n{plateNum} | {description} | {environment} | {date.strftime('%d/%m/%Y')} | {time} | {status} | {amount}")
    except Exception as e:
        print("Something went wrong when we append the accident report:", e)

    
# Function to print accident reports
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

# Function to delete an accident report
def deleteReport(file):
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

def filter_claims(lines, status_filter):
    filtered_lines = []
    for index, line in enumerate(lines):
        if index == 0:
            filtered_lines.append(line)
        else:
            car_details, amounts, status_damaged = line.strip().split(" | ")[0], line.strip().split(" | ")[6], line.strip().split(" | ")[5]
            if status_filter == "p" and status_damaged.lower() == "paid":
                filtered_lines.append(line)
            elif status_filter == "u" and status_damaged.lower() == "unpaid":
                filtered_lines.append(line)
            elif status_filter == "o":
                filtered_lines.append(line)
    return filtered_lines


# Function to print damage claims
def printDamageClaims(file):
    try:
        with open(file, 'rt') as filehandler:
            accidentlines = filehandler.readlines()

        while True:
            status_choice = keyboard_input(str, "Do you want to show paid (p), unpaid (u), or all status (o)? ", "Response must be a single character (p, u, o)")
            if status_choice.lower() in ["p", "u", "o"]:
                break
            else:
                print("Invalid input, please try again.")

        filtered_claims = filter_claims(accidentlines, status_choice.lower())

        print("\nDamage Claims:")
        for index, line in enumerate(filtered_claims):
            car_details, description, environment, date, time, status, amount = line.strip().split(" | ")
            if index == 0:
                print(f"{'No.':<5}{car_details:<10}{amount:<10}{status:<11}")
                print("="*35)
            else:
                print(f"{index:<5}{car_details:<10}{amount:<10}{status:<10}")

        status_choice = keyboard_input(str, "Do you want to continue for payment claims? [y/n]: ", "Response must be a string")
        if status_choice.lower() == 'y':
            while status_choice.lower() not in ['y', 'n']:
                status_choice = input("Please enter y or n: ")
            else:
                changeStatus(filtered_claims, file)

    except Exception as e:
        print("Something went wrong when printing the reports:", e)

    return

def changeStatus(filtered_claims, file):
    try:
        with open(file, "rt") as filehandler:
            lines = filehandler.readlines()
        data = [line.strip().split(" | ") for line in lines]

        index_choice = keyboard_input(int, "Enter the number from the list: ", "Index must be an Integer")
        if index_choice <= 0 or index_choice >= len(filtered_claims):
            print("Invalid index.")
        else:
            car_details, description, environment, date, time, status, amount = filtered_claims[index_choice].strip().split(" | ")
            if status.lower() == "unpaid":
                choice_paid = keyboard_input(str, f"Do you want to fully pay the amount [RM {amount}] for plate number [{car_details}]? [y/n]: ", "Response must be a string")
                if choice_paid.lower() == 'y':
                    for i, line in enumerate(data):
                        if line[0] == car_details and line[5].lower() == "unpaid":
                            data[i][5] = "paid"
                            data[i][6] = "0"
                            break

                    new_lines = [" | ".join(map(str, i)) + "\n" for i in data]
                    new_lines[-1] = new_lines[-1].strip()
                    with open(file, "wt") as filehandler:
                        filehandler.writelines(new_lines)
                    print("Damage claims successfully updated.")
                    print("Done! You have successfully paid.")
                else:
                    print("Payment not processed.")
            else:
                print("Selected claim is already paid.")

    except Exception as e:
        print("Something went wrong when updating the report:", e)


file = "accident.txt"
cars = "cars.txt"
booking = "booking.txt"

createFile(file)
doMenu(file, cars, booking)
