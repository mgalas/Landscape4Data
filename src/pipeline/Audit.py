class Audit:
    data = []
    auditData = []
    count = 0
    def __init__(self, data):
        self.data = data
        self.auditData = []


    # Removes rows even if one of the data items are blank
    def removeBlankRows(self):
        self.auditData = []
        for item in self.data:
            allCorrect = True
            for data in item:
                if data == '':
                    allCorrect = False
                    break
            if allCorrect:
                self.auditData.append(item)

    def getAuditedData(self):
        print("Auditing Data...")
        self.removeBlankRows()
        print("Data Audited.")
        return self.auditData
