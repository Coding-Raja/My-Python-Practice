#--------------------------------------------------------------------------------------

# creating a simple calculator using python

try:
    n1 = float(input("\nEnter first number : "))
    n2 = float(input("\nEnter second number : "))
    ch = input("\nEnter operator (+, -, *, /) : ")

    if ch == '+':
        print("\nAddition is : ", n1 + n2)
    elif ch == '-':
        print("\nSubtraction is : ", n1 - n2)
    elif ch == '*':
        print("\nMultiplication is : ", n1 * n2)
    elif ch == '/':
        if n2 == 0:
            print("\nError: Division by zero is not allowed!")
        else:
            print("\nDivision is : ", n1 / n2)
    else:
        print("\nChoose a Valid Operator")

except ValueError:
    print("\nError: Please enter valid numbers!")
except Exception as e:
    print(f"\nAn error occurred: {e}")

"""
Here we use a simple logic in python for a calculator. We use try to catch the error if any.
And we also use the some conditions to check whether the input is correct or logic is correct.
And we also use Type Casting to convert the string input to the numbers.
"""    
