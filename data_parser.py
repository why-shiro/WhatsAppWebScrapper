import json


class NumberProcessor:
    def __init__(self):
        f = open("elements.json")
        self.elementsData = json.load(f)

    def addElement(self, name: str, telNo: str, isGroup: str, y_index: int):
        for element in self.elementsData:
            if name in element:
                print("Nope")
            else:
                self.elementsData[name] = {"isGroup":isGroup,"phoneNum":telNo,"y_index":y_index}
        with open("elements.json", "w") as f:
            f.write(str(self.elementsData).replace("'", "\""))
            f.close()
