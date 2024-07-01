# has-a
class Passport:

    def __init__(self,country,passportnumber):
        self.country = country
        self.passportnumber = passportnumber

    def __str__(self):
        return f"Country: {self.country} \ n Passport Number: {self.passportnumber}"


class Customer:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""
        # Customer has a passport
        # 
        #
        self.passport = None

    def __str__(self):
        message = f"First Name: {self.firstname}"
        message = message + f"Last Name: {self.lastname}\n"
        message = message + f"IC Number: {self.icnumber}\n"
        if self.passport != None:
            message = message + self.passport.__str__()


peter = Customer("Parker", "Peter")
passport = Passport("UK", "E0202932")
peter.passport = passport
print(peter)
