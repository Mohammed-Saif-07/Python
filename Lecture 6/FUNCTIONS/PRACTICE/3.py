n = int(input("enter no: "))

def calFact(n):
    fact = 1
    for i in range(1,1+n):
        fact *= i
    print(fact)

calFact(n)