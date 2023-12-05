# reading days from user
days = int(input("Enter number of days: "))

# print number of years
print("Years:", int(days // 365))

# updating days
days = days % 365

# printing number of weeks
print("Weeks:", int(days // 7))

# updating days
days = days % 7

# printing number of days
print("Days:", int(days))
