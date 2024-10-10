num = int (input("Enter Any Positive number:"))
try:
    if num>=0:
        raise ValueError("Positive number-input Number is correct")
    else:
        raise ValueError("Negative Number-input Number is InCorrect")
except ValueError as e:
    print(e)