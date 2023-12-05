# Initialize the tuple
cars = ('coupe', 'coupe', 'coupe', 'carbiolet', 'sedan')

# Use the count method to count the number of times 'coupe' appears in the tuple
fav = cars.count('coupe')

# Use the len method to calculate the length of the tuple
amt = len(cars)

# Calculate the percentage of 'coupe' elements in the tuple
percentage = (fav / amt) * 100

# Check if the percentage is more than 45% and print the appropriate message
if percentage > 45:
    print("Too many coupes in the garage.")
else:
    print("You are all set with cars.")
