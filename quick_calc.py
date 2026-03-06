class QuickCalc:
    def __init__(self):
        self.reset()

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def reset(self):
        self.current = 0
        self.result = 0

    def calculate(self, op, a, b):
        if op == '+':
            return self.add(a, b)
        elif op == '-':
            return self.subtract(a, b)
        elif op == '*':
            return self.multiply(a, b)
        elif op == '/':
            return self.divide(a, b)
        else:
            return "Error: Unknown operation"
