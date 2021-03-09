def prime(num):
    isPrime = True
    if num == 1:
        isPrime = False
    else:
        for i in range(2, num):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if(num%i==0):
                isPrime = False
                break
 
    return isPrime

#Main Code
for num in range(1,101):
    #Divisible by both 3 and 5
    if(num%3 == 0 and num%5 == 0):
        print("FizzBuzz")
    #Divisible by 3
    elif(num%3==0):
        print("Fizz")
    #Divisible by 5
    elif(num%5==0):
        print("Buzz")
    #Check if Prime
    elif(prime(num)):
        print("Prime")
    else:
        print(num)
        
        

        
