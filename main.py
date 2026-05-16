from operations import Operation 
from operations import Calculator 
from operations import Add
from operations import Power


class Multiplication(Operation):
    def execute(self, a, b):
        return a * b
    
    
calc = Calculator()
calc.register_operation("add", Add())
calc.register_operation("mult", Multiplication())
calc.register_operation("power", Power())

while True:
        print("\n--------------------------------")
        user_op = input("Enter operation (add, mult, power) or 'exit' to quit: ").strip().lower()
        
        if user_op == 'exit':
            print("Goodbye!")
            break
            
        if user_op not in ["add", "mult", "power"]:
            print("Invalid operation! Please choose add, mult, or power.")
            continue
            
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue
            
        result = calc.calculate(user_op, num1, num2)
        print(f"Result: {result}")

