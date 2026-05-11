from calc import Operation 
from calc import Calculator 


class Multiplication(Operation):
    def execute(self, a, b):
        return a * b
    
    
calc = Calculator()
calc.register_operation("multiply", Multiplication())