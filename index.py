"""
Printing fibonacci sequence 
"""

try:
    Fibonacci_Terms = int(input("Enter n to generate a Fibonacci sequence: "))

    # Set the first two numbers in the Fibonacci sequence
    Base1 = 0
    Base2 = 1

    Base1_Copy = Base1
    Base2_Copy = Base2

    if Fibonacci_Terms <= 0:
        print("INVALID:It should have a positive value")

    elif Fibonacci_Terms == 1:
        print(Base1, end = ' ')

    else:
        print(Base1, Base2, end = ' ')

    for i in range(Fibonacci_Terms - 2): #I set the range to n - 2 because 0 and 1 are always printed initially

        #Determine the next number by summing the two previous numbers
        Fibonacci_Sum = Base1_Copy + Base2_Copy

        print(Fibonacci_Sum, end = ' ')

        # Update the copy of base1 and base2 for the next iteration
        Base1_Copy = Base2_Copy
        Base2_Copy = Fibonacci_Sum

except ValueError:
    print("INVALID:Enter a number only")
 