
try:
    a = int(input("enter a value:"))
    b = int(input("enter a value:"))
    print(a/b)

except ZeroDivisionError as e:
    print("can't divide by Zero: ", e)
except ValueError as e:
    print("invalid input:", e)
except Exception as e:
    print(e)
