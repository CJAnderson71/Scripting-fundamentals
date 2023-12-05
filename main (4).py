# Step 1: Define a counter for the sum named total_sum
total_sum = 0

# Step 2: Define a for loop with an even range for numbers between 5 and 55.
# We can use the range function with a step of 2 to generate even numbers.
for num in range(6, 56, 2):  # Starting from 6 (the first even number) up to 56 (exclusive) with a step of 2.
    
    # Step 3: Add each looped number to the sum.
    total_sum += num

# Step 4: Outside the loop, print out the total sum.
print(total_sum)
