try:
    numerator=int(input("enter numerator:"))
    denominator=int(input("enetr denominator:"))
    result=numerator/denominator
    print(f"Result:{result}")
except ZeroDivisionError:
    print("Error:Cannot divide by zero.")
except ValueError:
    print("Error:Please enter valid integers")