# Initialize variables
a, b = 1, 2
sum_even = 0

# Continue generating Fibonacci sequence while the current term (b) is less than or equal to 4 million
while b <= 4000000:
    # Check if the current term is even
    if b % 2 == 0:
        # Add the even term to the sum
        sum_even += b

    # Generate the next Fibonacci term
    a, b = b, a + b

# Print the result
print("The sum of even-valued terms in the Fibonacci sequence below 4 million is:", sum_even)
