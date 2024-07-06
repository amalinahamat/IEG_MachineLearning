class Student:
    def __init__(self,name,department,id_card = None):
        self.name = name
        self.department = department
        self.id_card = id_card

    def __str__(self):
        return self.name + " - " + self.department + " - " + str(self.id_card)
    