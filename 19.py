class Calculator:
    def __init__(self, num1, operator, num2):
        self.num1 = num1
        self.operator = operator
        self.num2 = num2

    def add(self):
        print(self.num1 + self.num2)

    def subtract(self):
        print(self.num1 - self.num2)

    def divide(self):
        print(self.num1 / self.num2)

    def multiply(self):
        print(self.num1 * self.num2)

    # Power - Radical - Sin - Cos - Factorial - Log


def main():
    number1 = int(input("Number : "))
    operator = input("Operator : ")
    number2 = int(input("Number : "))

    calc = Calculator(number1, operator, number2)

    print("Result : ", end="")

    if calc.operator == "+":
        calc.add()
    elif calc.operator == "-":
        calc.subtract()
    elif calc.operator == "/":
        calc.divide()
    elif calc.operator == "*":
        calc.multiply()
    else:
        print("Invalid Operator. Try again.")
        main()


main()
