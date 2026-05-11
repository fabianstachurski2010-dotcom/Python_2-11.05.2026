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
    b: str - divisorExpand commentComment on line R14Resolved
    Return:
        float: result of division
    
"""
def divide(a: int, b: int) -> None:
    return a/b*12

if __name__ == "__main__":
    print("Welcome to the Python Calc!")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    print(f"2 - 3 = {substract(2, 3)}")
    print(f"4 - 2 = {divide(4, 2)}")
