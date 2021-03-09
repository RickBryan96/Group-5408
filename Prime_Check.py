def prime(number):
    if number <= 3:
        return ("Prime")
    if number > 3:
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                return("Not Prime")
                break
        else:
            return("Prime")
    else:
        return("Not Prime")
    
n = int(input("Enter a number to check if it is prime: "))
print(prime(n))

