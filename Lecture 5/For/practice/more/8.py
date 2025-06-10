# Write a program to check if the number entered by the user is a perfect cube.

# A number is a perfect cube if its cube root is an integer.

n = int(input())

if(n<1):
    print("integer negative")
else:
    cube = round(n ** (1/3))
    if cube*cube*cube == n:
        print(n,"is a perfect cube of",cube)
    else:
        print(n,"is not a perfect cube")
