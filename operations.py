
"""
    Performs division
    Params:
    a: int - dividor
    b: int - divisor
    Return:
        float: result of division
    
"""

class Operation:
    def execute(self, a, b):
        raise NotImplementedError("Each operation must implement execute()")

class Add(Operation):
    def execute(self, a, b):
        return a + b

class Multiply(Operation):
    def execute(self, a, b):
        return a * b

class Power(Operation):
    def execute(self, a, b):
        return a ** b

class Calculator:
    def __init__(self):
        self.operations = {}

    def register_operation(self, name, op_obj):
        self.operations[name] = op_obj

    def calculate(self, name, a, b):
        if name not in self.operations:
            return "Operation not found!"
        return self.operations[name].execute(a, b)
    
if __name__ == "__main__":
    calc = Calculator()
    calc.register_operation("add", Add())
    calc.register_operation("mult", Multiply())
    calc.register_operation("power", Power())
    print("Welcome to the Python Calc! \n")
    print(f"2 + 3 = {calc.calculate('add', 2, 3)}")
    print(f"2 * 3 = {calc.calculate('mult', 2, 3)}")
    print(f"2 ** 3 = {calc.calculate('power', 2, 3)}")