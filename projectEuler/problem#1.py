# Initialize the sum
total_sum = 0

# Iterate through all numbers below 1000
for i in range(1, 1000):
    # Check if the number is a multiple of 3 or 5
    if i % 3 == 0 or i % 5 == 0:
        # Add the multiple to the sum
        total_sum += i

# Print the result
print("The sum of multiples of 3 or 5 below 1000 is:", total_sum)

