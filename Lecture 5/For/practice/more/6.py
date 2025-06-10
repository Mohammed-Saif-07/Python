# //-----------------Print if a number n is prime or not (Input n from the user)----------------

n = int(input())

if(n<=1):
    print(n,"not a prime number")
else:
    isPrime = True
    for i in range(2,n):
        if(n%i==0):
            isPrime = False
            break

    if isPrime:
        print(n,"is a prime no")
    else:
        print(n,"is not a prime no")