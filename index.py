"""
Printing fibonacci sequence 
"""

try:
    fibonacci_terms = int(input("Enter n to generate a Fibonacci sequence: "))
    fibonacci_count = 0 
    # Set the first two numbers in the Fibonacci sequence
    base1 = 0
    base2 = 1

    base1_copy = base1
    base2_copy = base2

    if fibonacci_terms <= 0:
        print("INVALID:It should have a positive value")

    elif fibonacci_terms == 1:
        print(base1, end = ' ')

    else:
        print(base1, base2, end = ' ')

    for i in range(fibonacci_terms - 2): #I set the range to n - 2 because 0 and 1 are always printed initially.
        #Determine the next number by summing the two previous numbers
        fibonacci_sum = base1_copy + base2_copy

        if fibonacci_count < fibonacci_terms :
            print(fibonacci_sum, end = ' ')
            fibonacci_count += 1
            # Update the copy of base1 and base2 for the next iteration
            base1_copy = base2_copy
            base2_copy = fibonacci_sum

except ValueError:
    print("INVALID:Enter a number only")
 