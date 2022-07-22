import re
class ValidCarNumber:
    number = "01KG777BAD"

    def __init__(self, number):
        self.number = number

    def is_valid_number(self):
        is_valid = re.search("0([0-9]{1})KG([0-9]{3}[A-Z]{3})", self.number)

        try:
            if self.number[is_valid.start():is_valid.end()] == self.number:
                return "Valid Car Number"
            else:
                raise ValueError
        except:
            return "Invalid Car Number"
    print("Invalid Car Number")