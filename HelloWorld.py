for i in range(20):
    for j in range(4-i):
        print("*",bg)
    print()


gender = input("enter gender as F/M")
if gender == 'F' or gender == 'f':
    print("Female")
else:
    print("Male")
