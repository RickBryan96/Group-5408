# Anthony Serrano
# Part D
# This function calculates the fibonacci sum up to a
# user inputted number
def fibosum(n):
    if(n <= 0):
        return 0
    
    # Create a list of n+1 elements full of zeros
    fibo = [0] * (n+1)
    fibo[1] = 1
    
    # Sum of the first two fibonacci numbers
    fsum = fibo[0] + fibo[1]
    
    # Find the next fibonacci term and add it to the sum
    # of all the numbers
    for i in range(2,n+1):
        fibo[i] = fibo[i-1] + fibo[i-2] # next term
        fsum = fsum + fibo[i] # sum of all current terms
    return fsum

# body
n = int(input('Enter a number to find the fibonacci sum up to: '))
print('The fibonacci sum up to', n, 'is: ',fibosum(n))