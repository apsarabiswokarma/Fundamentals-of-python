
a, b = 1, 2
sum_even = 0


while b <= 4000000:
   
    if b % 2 == 0:  
        sum_even += b 
        
    a, b = b, a + b
print("The sum of even-valued terms in the Fibonacci sequence below 4 million is:", sum_even)
