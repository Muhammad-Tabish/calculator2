from addition import Addition
result = Addition.add (100,200)
class Calculator:


    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)  # make use of add() from addition module
    @classmethod
    def sub(cls, num1, num2):
        return num1 - num2

    @classmethod
    def mult (cls, num1, num2):
        return num1 * num2


    @classmethod
    def div(cls, num1, num2):
        return num1 / num2


