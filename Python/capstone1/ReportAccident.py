from os.path import exists

class ReportAccident:
    def __init__ (self,accidents,cars,booking):
        self.accidents = accidents
        self.cars = cars
        self.booking = booking

    def create_file(self):
        if not exists (self.accidents):
            try:
                filehandler = open(self.accidents, "xt")
            except Exception as e:
                print("Something when wrong when the file is created!", e)
            else:
                print(f"File '{self.accidents}' created successfully.")
            finally:
                filehandler.close()

    @staticmethod
    def keyboardInput(datatype, caption, errorMessage):
        value = None
        isInvalid = True
        while isInvalid:
            try:
                value = datatype(input(caption))
            except:
                print(errorMessage)
            else:
                isInvalid = False
        return value

    def Menu(self):
        while True:
            print("-----------------------------")
            print("             MENU            ")
            print("0  -         EXIT            ")
            print("1  -   REPORTING ACCIDENT    ")
            print("2  -      DAMAGED CLAIM      ")
            print("-----------------------------")
            choice = self.keyboardInput(int, "Choice(0,1,2): ", "Choice must be Integer")
            if (choice == 0):
                print("Thanks!")
                break
            elif (choice == 1):
                self.cars_display()
            elif (choice == 2):
                self.booking_display()
            else:
                print("Invalid choice. Please try again.")

    
    def cars_display(self):
        if exists(self.cars):
            try:
                with open(self.cars, "rt") as carsfile:
                    content = carsfile.read()
                    print(f"Contents of '{self.cars}':\n{content}")

            except Exception as e:
                print("Something went wrong when reading the cars file!", e)
        
        else:
            print("cars file does not exist")

    def booking_display(self):
        if exists(self.booking):
            try:
                with open(self.booking, "rt") as bookingfile:
                    content = bookingfile.read()
                    print(f"Contents of '{self.booking}':\n{content}")

            except Exception as e:
                print("Something went wrong when reading the booking file!", e)
        
        else:
            print("Booking file does not exist")


report = ReportAccident("accidents.txt", "cars.txt", "booking.txt")
report.create_file()
report.Menu()










