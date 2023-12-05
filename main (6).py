# Iterate over numbers from 10 to 100 (inclusive)
for num in range(10, 101):
    # Check if the number is equal to zero
    if num == 0:
        # Skip the current iteration and move to the next number
        continue

    # Check if the number is not divisible by 5
    elif num % 5 != 0:
        # Skip the current iteration and move to the next number
        continue

    # Check if the number is not of integer type
    elif not isinstance(num, int):
        # Skip the current iteration and move to the next number
        continue

    # Check if the number is equal to 95
    elif num == 95:
        # Break out of the loop prematurely
        break

    # If none of the above conditions are met, the number has passed all checks
    else:
        pass
        # No specific action needed, use the 'pass' statement

    # Print the number if it meets the conditions specified
    print(num)
