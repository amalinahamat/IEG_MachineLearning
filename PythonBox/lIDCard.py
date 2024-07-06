class IDCard:
    def __init__(self, row_number, isBarcoded):
        self.row_number = row_number
        self.isBarcoded = isBarcoded

    def __str__(self):
        return self.row_number + " : " + str(self.isBarcoded)
    