try:
    n = int(input("Enter n to generate a Fibonacci sequence: "))
    count = 0 
    # Set the first two numbers in the Fibonacci sequence
    n1 = 0
    n2 = 1

    if n <= 0:
        print("It should have a value of 1 or higher")
    elif n == 1:
        print(n1, end = ' ')
    else:
        print(n1, n2, end = ' ')

    for i in range(n - 2): #I set the range to n - 2 because 0 and 1 are always printed initially.
        #Determine the next number by summing the two previous numbers
        n3 = n1 + n2
        if count < n :
            print(n3, end = ' ')
            count += 1
            # Update n1 and n2 for the next iteration
            n1 = n2
            n2 = n3
except ValueError:
    print("INVALID:Enter a number only")
 