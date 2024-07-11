from os.path import exists
from datetime import datetime

# Function to handle generic keyboard input with validation
def keyboard_input(datatype, caption, errorMessage, defaultValue=None):
    value = None
    isInvalid = True
    while isInvalid:
        try:
            # Check for default value
            if defaultValue is None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if value.strip() == "":
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
    while choice != 0:
        print("---------------------------")
        print("|         MENU            |")
        print("| 0 -     EXIT            |")
        print("| 1 - Reporting Accident  |")
        print("| 2 - List of Report      |")
        print("| 3 - Delete Report       |")
        print("| 4 - Damage Claim        |")
        print("---------------------------")
        choice = keyboard_input(int, "Choice [0, 1, 2, 3, 4]: ", "Choice must be Integer")
        if choice == 0:
            print("Thank you for using our system")
            break
        elif choice == 1:
            selectCar(cars, booking, file)
        elif choice == 2:
            printReport(file)
        elif choice == 3:
            deleteReport(file)
        elif choice == 4:
            printDamageClaims(file)

# Function to create a file if it doesn't exist
def createFile(file):
    if not exists(file):
        try:
            filehandler = open(file, 'xt')
        except Exception as e:
            print("Something went wrong when we create the file:", e)
        else:
            createTitle(file)
        finally:
            filehandler.close()

# Function to create the title/header in the file
def createTitle(file):
    try:
        with open(file, 'wt') as filehandler:
            filehandler.write("Car Detail | Description | Environment Condition | Date | Time | Status | Amount\n")
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
                print("=" * 80)
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

# Function to handle generic keyboard input with validation
def keyboard_input(input_type, caption, errorMessage, defaultValue=None):
    value = None
    isInvalid = True
    while isInvalid:
        try:
            if defaultValue is None:
                value = input_type(input(caption))
            else:
                value = input(caption)
                if value.strip() == "":
                    value = defaultValue
                else:
                    value = input_type(value)
        except ValueError:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def accidentReport(file, car_choice, selected_booking):
    try:
        car_platNo, _, startRent, endRent = selected_booking.split(" | ")

        accident_date = date_input("Date (DD/MM/YYYY): ", "Date must be in DD/MM/YYYY format.")
        startRent = datetime.strptime(startRent, "%d/%m/%Y").date()
        endRent = datetime.strptime(endRent, "%d/%m/%Y").date()

        if startRent <= accident_date <= endRent:
            plateNum = car_platNo
            description = keyboard_input(str, "\nDescription[Light/Medium/Extreme Accident]: ", "Description must be String.")
            environment = keyboard_input(str, "Environment Condition[Road:Bumpy/Slippery] | [Weather:Sunny/Rain]: ", "Environment Condition must be String.")
            date = accident_date.strftime("%d/%m/%Y")
            time = time_input("Time (09:35 PM): ", "Time must be in 12-Hour format.")
            status = keyboard_input(str, "Status[Paid/Unpaid]: ", "Status must be String.")
            amount = keyboard_input(str, "Amount [RM]: ", "Amount must be String.")

            with open(file, "at") as filehandler:
                filehandler.write(f"{plateNum} | {description} | {environment} | {date} | {time} | {status} | {amount}\n")
        else:
            print("Accident Date must be within the rental period")

    except Exception as e:
        print("Something went wrong when reporting accident:", e)

def printReport(file):
    try:
        with open(file, "rt") as filehandler:
            print("\n---------------------")
            print("| Report           |")
            print("---------------------")
            print(filehandler.read())
    except Exception as e:
        print("Something went wrong when reading the report file:", e)

def deleteReport(file):
    try:
        with open(file, "rt") as filehandler:
            lines = filehandler.readlines()

        print("\n---------------------")
        print("| Report           |")
        print("---------------------")
        for i, line in enumerate(lines):
            print(f"{i}. {line.strip()}")

        delete_index = keyboard_input(int, "\nEnter the number of the report to delete: ", "Choice must be an integer.")
        if 0 < delete_index < len(lines):
            del lines[delete_index]
            with open(file, "wt") as filehandler:
                filehandler.writelines(lines)
            print("Report deleted successfully.")
        else:
            print("Invalid choice, please select a valid report number.")
    except Exception as e:
        print("Something went wrong when deleting the report:", e)

def printDamageClaims(file):
    try:
        with open(file, "rt") as filehandler:
            lines = filehandler.readlines()

        damage_claims = []
        for line in lines[1:]:
            details = line.strip().split(" | ")
            if "Extreme Accident" in details[1]:
                damage_claims.append(line)

        print("\n---------------------")
        print("| Damage Claims     |")
        print("---------------------")
        for claim in damage_claims:
            print(claim.strip())
    except Exception as e:
        print("Something went wrong when reading the report file:", e)

# Main program execution
if __name__ == "__main__":
    cars_file = "cars.txt"
    booking_file = "booking.txt"
    report_file = "accident.txt"
    createFile(report_file)
    doMenu(report_file, cars_file, booking_file)
