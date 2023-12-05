# On the first line, create the following array

numbers = [34, 9, 32, 91, 58, 13, 77, 21, 56]

# Next, print the array numbers

print(numbers)

# fetch the user input count for the number of elements to fetch from the array.

n = int(input("How many elements to fetch: "))

# and then outputs those elements.

for i in range(n):
    print(numbers[i], end=' ')

print()

# Finally, print out the slice of the array from the first element to the nth element.

print(numbers[:n])
