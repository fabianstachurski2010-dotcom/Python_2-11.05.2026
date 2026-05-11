def add(a, b):
    return a + b
def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

"""
    Performs division
    Params:
    a: int - dividor
    b: int - divisor
    Return:
        float: result of division
    
"""
def divide(a: int, b: int) -> float:
    return a/b

class Operation:
    def execute(self, a, b):
        raise NotImplementedError("Each operation must implement execute()")

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
    print("Welcome to the Python Calc!")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    print(f"2 - 3 = {substract(2, 3)}")
    print(f"4 / 2 = {divide(4, 2)}")
