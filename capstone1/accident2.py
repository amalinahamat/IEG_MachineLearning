from os.path import exists
from datetime import datetime

# 1. InputHandler Class
# This class handles user input, ensuring the data is valid and correctly formatted.

# keyboard_input: Handles generic input and ensures it matches the expected datatype. If a default value is provided, it uses this value when the user inputs an empty string.
# date_input: Ensures the date input is in the "DD/MM/YYYY" format and handles validation.
# time_input: Ensures the time input is in the "12-Hour format" (like "9:35pm") and handles validation.

class InputHandler:

    # Function to handle generic keyboard input with validation
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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


# 2. FileManager Class
# This class handles file creation and writing headers.

# createFile: Checks if the file exists; if not, it creates the file and adds a header.
# createTitle: Writes a header to the file, containing column titles for the accident report.
    
class FileManager:

    # Function to create a file if it doesn't exist   
    @staticmethod         
    def createFile(accident_file):
        if not exists(accident_file):
            try:
                with open(accident_file, 'xt') as filehandler:
                    FileManager.create_title(accident_file)
            except Exception as e:
                print("Something went wrong when creating the file:", e)


    # Function to create the title/header in the file
    @staticmethod
    def createTitle(accident_file):
        try:
            with open(accident_file, 'wt') as filehandler:
                filehandler.write("Car Detail | Description | Environment Condition | Date | Time | Status | Amount")
        except Exception as e:
            print("Something went wrong when we create the header:", e)   


# 3. AccidentReport Class
# This is the main class that manages the menu, displaying options, and handling operations like reporting accidents, listing reports, deleting reports, and handling damage claims.

class AccidentReport:

    # init: Initializes the class with filenames for cars, bookings, and accident reports. It also ensures the accident file exists by creating it if necessary.
    def __init__(self, cars_file, booking_file, accident_file):
        self.cars_file = cars_file
        self.booking_file = booking_file
        self.accident_file = accident_file
        FileManager.createFile(self.accident_file)
        
    # Prints text centered within a given width.    
    def print_centered(self,text, width):
        print(text.center(width))

    # Prints colored text centered within a given width
    def print_colored_centered(self,text, color_code, width):
        print(f"\033[{color_code}m{text.center(width)}\033[0m")

    # Main menu function
    # Displays the main menu with options for reporting an accident, listing reports, deleting a report, and managing damage claims. It handles user input to navigate to the appropriate functionality.
    def display_menu(self):
        choice = -1
        while (choice != 0):
            width = 150  # You can adjust this width as per your console's width
            print("\033[1;34m" + "-" * width + "\033[0m")  # Blue color for border
            self.print_colored_centered("MENU", "1;32", width)  # Green color for the title
            print("\033[1;34m" + "-" * width + "\033[0m")  # Blue color for border
            self.print_colored_centered("0 - EXIT", "1;33", width)  # Yellow color for options
            self.print_colored_centered("1 - Reporting Accident", "1;33", width)  # Yellow color for options
            self.print_colored_centered("2 - List of Report", "1;33", width)  # Yellow color for options
            self.print_colored_centered("3 - Delete Report", "1;33", width)  # Yellow color for options
            self.print_colored_centered("4 - Damage Claim", "1;33", width)  # Yellow color for options
            print("\033[1;34m" + "-" * width + "\033[0m")  # Blue color for border
            choice = InputHandler.keyboard_input(int, "Choice [0, 1, 2, 3, 4]: ", "Choice must be Integer")
            if (choice == 0):
                print("Thank you for using our system")
                break
            elif (choice == 1):
                self.selectCar()
            elif (choice == 2):
                self.printReport()
            elif (choice == 3):
                self.deleteReport()
            elif (choice == 4):
                self.printDamageClaims()

    # Filters cars based on their status (active, inactive, or all).
    def filter_cars(self,lines, status_filter):
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
    # Displays the list of cars and allows the user to select one. It then displays bookings related to the selected car and allows the user to choose a booking for accident reporting.
    def selectCar(self):

        width = 150
        try:
            with open(self.cars_file, "rt") as filehandler:
                lines = filehandler.readlines()

            while True:
                status_choice = InputHandler.keyboard_input(str, "Do you want to show active (a), inactive (i), or all cars (o)? ", "Response must be a single character (a, i, o)")
                if status_choice.lower() in ["a", "i", "o"]:
                    break
                else:
                    print("Invalid input, please try again.")

            filtered_lines = self.filter_cars(lines, status_choice.lower())

            print("\nSelect a car from the list:")

            for index, line in enumerate(filtered_lines):
                platNo, modelCar, nameCar, colorCar, statusCar = line.strip().split(" | ")
                if index == 0:
                    header = f"{'No.':<8}{platNo:<15}{modelCar:<15}{nameCar:<15}{colorCar:<15}{statusCar:<10}"
                    self.print_colored_centered(header, "1;34", width)  # Blue color for header
                    self.print_colored_centered("="*width, "1;34", width)  # Blue color for separator   
                else:
                    car_details = f"{index:<8}{platNo:<15}{modelCar:<15}{nameCar:<15}{colorCar:<15}{statusCar:<10}"
                    self.print_colored_centered(car_details, "1;32", width)  # Green color for car details

            choice = InputHandler.keyboard_input(int, "\nEnter the number of the car: ", "Choice must be an integer.")

            if choice < 1 or choice >= len(filtered_lines):
                print("Invalid choice, please select a valid car number.")
                return self.selectCar()
            else:
                # Read and display booking.txt
                selected_car = filtered_lines[choice].strip().split(" | ")[0]

                with open(self.booking_file, "rt") as booking_filehandler:
                    booking_lines = booking_filehandler.readlines()

                print("\nBooking Details:")

                bookingRelated = [line.strip() for line in booking_lines if line.startswith(selected_car)]
                for booking_index, booking_line in enumerate(bookingRelated):
                    booking_details = f"{booking_index + 1}. {booking_line}"
                    self.print_colored_centered(booking_details, "1;36", width)  # Cyan color for booking details


                if bookingRelated:
                    booking_choice = InputHandler.keyboard_input(int, "\nEnter the number of the booking: ", "Choice must be an integer.")
                    if booking_choice < 1 or booking_choice > len(bookingRelated):
                        print("Invalid choice, please select a valid booking number.")
                    else:
                        selected_booking = bookingRelated[booking_choice - 1]
                        self.accidentReport(selected_car, selected_booking)        
                else:
                    print("No booking found for the selected car.")
                    return None
                            
        except Exception as e:
            print("Something went wrong when selecting a car:", e)
            return None
        
    # Function to create an accident report
    # Collects accident details from the user and validates that the accident date is within the booking period. It then appends the report to the accident file.
    def accidentReport(self,car_choice, selected_booking):

        try:
            car_platNo, _, startRent, endRent = selected_booking.split(" | ")

            accident_date = InputHandler.date_input("Date (DD/MM/YYYY): ", "Date must be in DD/MM/YYYY format.")
            startRent = datetime.strptime(startRent, "%d/%m/%Y").date()
            endRent = datetime.strptime(endRent, "%d/%m/%Y").date()

            if startRent <= accident_date <= endRent:
                plateNum = car_platNo
                description = InputHandler.keyboard_input(str, "\n\033[1mDescription\033[0m[Light/Medium/Extreme Accident]: ", "Description must be String.")
                environment = InputHandler.keyboard_input(str, "\n\033[1mEnvironment Condition\033[0m[Road:Bumpy/Slippery] | [Weather:Sunny/Rain]: ", "Environment Condition must be String.")
                time = InputHandler.time_input("\n\033[1mTime\033[0m (9:35pm): ", "Time must be in 12-Hour format.")
                status = InputHandler.keyboard_input(str, "\n\033[1mStatus\033[0m[Paid/Unpaid]: ", "Status must be String.")
                amount = InputHandler.keyboard_input(str, "\n\033[1mAmount\033[0m [RM]: ", "Amount must be String.")

                with open(self.accident_file, "at") as filehandler:
                    filehandler.write(f"\n{plateNum} | {description} | {environment} | {accident_date.strftime('%d/%m/%Y')} | {time} | {status} | {amount}")
                print("Accident report successfully added.")
            else:
                print(f"Accident date {accident_date.strftime('%d/%m/%Y')} is not within the booking period from {startRent.strftime('%d/%m/%Y')} to {endRent.strftime('%d/%m/%Y')}.")

        except Exception as e:
            print("Something went wrong when we append the accident report:", e)
        
    # Function to print accident reports
    # Reads and displays accident reports from the accident file
    def printReport(self):
        width = 150  # Set the width of the console display

        try:
            with open(self.accident_file, "rt") as filehandler:
                lines = filehandler.readlines()
            print("\n\n")
            
            # Header
            header = f"{'No.':<8}{'Car Detail':<15}{'Description':<20}{'Environment':<20}{'Date':<15}{'Time':<15}{'Status':<20}{'Amount':<19}"
            self.print_colored_centered(header, "1;34", width)  # Blue color for header
            self.print_colored_centered("=" * width, "1;34", width)  # Blue color for separator

            for index, line in enumerate(lines):
                car_detail, description, environment, date, time, status, amount = line.strip().split(" | ")
                if index == 0:
                    continue  # Skip the header row in the file
                else:
                    report_line = f"{index:<8}{car_detail:<15}{description:<20}{environment:<20}{date:<15}{time:<15}{status:<20}{amount:<19}"
                    self.print_colored_centered(report_line, "1;32", width)  # Green color for report lines
            print("\n\n")

        except Exception as e:
            print("Something went wrong when we print the description:", e)


    # Function to delete an accident report
    # Reads and displays accident reports, allows the user to select one, and deletes the selected report.
    def deleteReport(self):
        width = 150
        try:
            with open (self.accident_file, "rt") as filehandler:
                lines = filehandler.readlines()

            # Header
            header = f"{'No.':<8}{'Car Detail':<15}{'Description':<20}{'Environment':<20}{'Date':<15}{'Time':<15}{'Status':<20}{'Amount':<19}"
            self.print_colored_centered(header, "1;34", width)  # Blue color for header
            self.print_colored_centered("=" * width, "1;34", width)  # Blue color for separator

            for index, line in enumerate(lines):
                    car_detail,description, environment, date, time, status, amount = line.strip().split(" | ")
                    if (index == 0):
                        continue
                    else:
                        report_line = f"{index:<8}{car_detail:<15}{description:<20}{environment:<20}{date:<15}{time:<15}{status:<20}{amount:<19}"
                        self.print_colored_centered(report_line, "1;32", width)  # Green color for report lines

            choice = InputHandler.keyboard_input(int, "Enter the number of the report to delete: ", "Choice must be an integer.")

            if 1 <= choice <= len(lines) - 1:
                lines.pop(choice)  # Remove the selected report
                
                # new_lines = [" | ".join(map(str, i)) + "\n" for i in lines]
                # new_lines[-1] = new_lines[-1].strip()

                with open(self.accident_file, "wt") as filehandler:
                    #filehandler.writelines(lines)
                    filehandler.write("\n".join(line.strip() for line in lines))
                print("Report deleted successfully.")
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Something went wrong when deleting the report:", e)

    # Filters damage claims based on their status (paid, unpaid, or all).
    def filter_claims(self, lines, status_filter):
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
    # Displays damage claims based on the filter and allows the user to change the status of a claim to 'paid'.
    def printDamageClaims(self):
        width = 150

        try:
            with open(self.accident_file, 'rt') as filehandler:
                accidentlines = filehandler.readlines()

            while True:
                status_choice = InputHandler.keyboard_input(str, "Do you want to show paid (p), unpaid (u), or all status (o)? ", "Response must be a single character (p, u, o)")
                if status_choice.lower() in ["p", "u", "o"]:
                    break
                else:
                    print("Invalid input, please try again.")

            filtered_claims = self.filter_claims(accidentlines, status_choice.lower())

            print("\nDamage Claims:")
            for index, line in enumerate(filtered_claims):
                car_details, description, environment, date, time, status, amount = line.strip().split(" | ")
                if index == 0:
                    header = f"{'No.':<8}{'Car Details':<15}{'Amount':<10}{'Status':<10}"
                    self.print_colored_centered(header, "1;34", width)  # Blue color for header
                    self.print_colored_centered("=" * width, "1;34", width)  # Blue color for separator
                else:
                    report_line = f"{index:<8}{car_details:<15}{amount:<10}{status:<10}"
                    self.print_colored_centered(report_line, "1;32", width)  # Green color for report lines

            status_choice = InputHandler.keyboard_input(str, "Do you want to continue for payment claims? [y/n]: ", "Response must be a string")
            if status_choice.lower() == 'y':
                while status_choice.lower() not in ['y', 'n']:
                    status_choice = input("Please enter y or n: ")
                else:
                    self.changeStatus(filtered_claims)

        except Exception as e:
            print("Something went wrong when printing the reports:", e)

        return

    # Updates the status of a selected claim to 'paid' and writes the updated data back to the accident file.
    def changeStatus(self, filtered_claims):

        width = 150
        try:
            with open(self.accident_file, "rt") as filehandler:
                lines = filehandler.readlines()
            data = [line.strip().split(" | ") for line in lines]

            index_choice = InputHandler.keyboard_input(int, "Enter the number from the list: ", "Index must be an Integer")

            if index_choice <= 0 or index_choice >= len(filtered_claims):
                print("Invalid index.")
            else:
                car_details, description, environment, date, time, status, amount = filtered_claims[index_choice].strip().split(" | ")
                if status.lower() == "unpaid":
                    choice_paid = InputHandler.keyboard_input(str, f"Do you want to fully pay the amount [RM {amount}] for plate number [{car_details}]? [y/n]: ", "Response must be a string")
                    if choice_paid.lower() == 'y':
                        for i, line in enumerate(data):
                            if line[0] == car_details and line[5].lower() == "unpaid":
                                data[i][5] = "paid"
                                data[i][6] = "0"
                                break

                        new_lines = [" | ".join(map(str, i)) + "\n" for i in data]
                        new_lines[-1] = new_lines[-1].strip()
                        with open(self.accident_file, "wt") as filehandler:
                            filehandler.writelines(new_lines)

                            self.print_colored_centered("Damage claims successfully updated.", "1;32", width)  # Green color for success message
                        self.print_colored_centered("Done! You have successfully paid.", "1;32", width)  # Green color for success message
                    else:
                        self.print_colored_centered("Payment not processed.", "1;31", width)  # Red color for cancel message
                else:
                    self.print_colored_centered("Selected claim is already paid.", "1;33", width)  # Yellow color for info message

        except Exception as e:
            self.print_colored_centered("Something went wrong when updating the report:", "1;31", width)  # Red color for error message


accident_report = AccidentReport(cars_file = "cars.txt", booking_file = "booking.txt", accident_file ="accident.txt" )

accident_report.display_menu()

