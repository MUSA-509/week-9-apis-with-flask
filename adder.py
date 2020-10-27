"""Add two numbers"""
import sys

def add_them_up(num1, num2):
    return num1 + num2

if __name__ == '__main__':
    # Note: argv[0] is the name of the program, argv[1] and argv[2]
    # should be the inputs
    if len(sys.argv) == 3:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    else:
        raise ValueError(f"Expected two numeric inputs, {len(sys.argv)} input")
    added_up = add_them_up(num1, num2)
    print(f"{num1} + {num2} = {added_up}")
