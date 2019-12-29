import datetime
age = 0
birth_year = int(input('Enter your birth  year : '))
current_year = datetime.datetime.now().year
if birth_year > current_year:
    print("Please enter correct birth year below- ", current_year)
else:
    age = current_year - birth_year
    print("Your age is: ", age)

