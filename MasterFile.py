#Rick Embrado
#Anthony Serrano
#Victor Santos
#Group 3 
#CSE 5408 Spring
#CSE LAB 4
#Master File 


#Prime porgram
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

#This program reverses the user input
def inputreverse(ui):
    words = ui.split(' ')
    reversed_input = ' '.join(reversed(words))
    return reversed_input

s = input("What would you like to reverse?" "\n") 
print(inputreverse(s))

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

# Part C of the Lab
from datetime import datetime
from pytz import timezone, utc

# This function converts the current time to military time
def get_mil_time(time12):
    time_format='%H:%M:%S'
    pstMilTime = time12.strftime(time_format)
    return pstMilTime


# Body 
# Get current time and convert from UTC to PST
now = datetime.now(tz=utc)
now = now.astimezone(timezone('US/Pacific'))
# Print current time in 12 hour format 
print ("Current time: ")
print (now.strftime("%I:%M:%S %p"))
# Print current time in Military time
print("Military Time: ")
print(get_mil_time(now))

#Part 5 of the Python Assignment
  
def isValid(password): 
  
    # for checking if password length 
    # is between 8 and 15 
    if (len(password) < 8 or len(password) > 15): 
        return False
  
    # to check space 
    if (" " in password): 
        return False
  
    if (True): 
        count = 0
  
        # check digits from 0 to 9 
        arr = ['0', '1', '2', '3',  
        '4', '5', '6', '7', '8', '9'] 
  
        for i in password: 
            if i in arr: 
                count = 1
                break
  
        if count == 0: 
            return False
  
    # for special characters 
    if True: 
        count = 0
  
        arr = ['@', '#','!','~','$','%','^', 
                '&','*','(',',','-','+','/', 
                ':','.',',','<','>','?','|'] 
  
        for i in password: 
            if i in arr: 
                count = 1
                break
        if count == 0: 
            return False
  
    if True: 
        count = 0
  
        # checking capital letters 
        for i in range(65, 91): 
  
            if chr(i) in password: 
                count = 1
  
        if (count == 0): 
            return False
  
    if (True): 
        count = 0
  
        # checking small letters 
        for i in range(90, 123): 
  
            if chr(i) in password: 
                count = 1
  
        if (count == 0): 
            return False
  
    # if all conditions fails 
    return True
  
# Driver code 
password1 = input("Enter Password: ")
  
if (isValid([i for i in password1])): 
    print("Valid Password") 
else: 
    print("Invalid Password!!!") 
    password1 = input("Enter Password: ") 