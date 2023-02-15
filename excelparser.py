import xlsxwriter

class Excel:

    def __init__(self):
        self.column = 0
        self.workbook = xlsxwriter.Workbook('contacts.xlsx')
        self.worksheet = self.workbook.add_worksheet()

    def addContact(self,element):
        self.worksheet.write(0, self.column, element)
        self.column += 1

    def closeFile(self):
        self.workbook.close()