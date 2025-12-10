from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    print(logo)
    function_dict = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        }

    first_number = float(input("What's the first number? "))
    store_memory = True
    while store_memory:
        for key in function_dict:
            print(key)
        operation = input("Pick an operation: ")
        second_number = float(input("What's the second number? "))

        # Select function stored in dictionary, determined by operation. Pass two numbers to chosen function.
        result = function_dict[operation](n1=first_number,n2=second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

        retain_memory = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ").lower()

        if retain_memory == 'n':
            store_memory = False
            print("\n" * 20)
            calculator()
        elif retain_memory == 'y':
            first_number = result

calculator()
