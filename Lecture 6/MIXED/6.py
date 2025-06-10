n = int(input())

def sumc(n):
    sum = 0
    for i in range(n):
        if(i%2!=0):
            sum += i
    return sum

print(sumc(n))