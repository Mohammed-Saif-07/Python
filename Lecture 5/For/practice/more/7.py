# Write a program that asks the user to input a positive integer m. Then, check if m is a perfect square or not.

# If m is a perfect square (like 1, 4, 9, 16, 25, etc.), print "m is a perfect square."

# Otherwise, print "m is not a perfect square."

n = int(input())

if(n<1):
    print("integer negatve")
else:
    sqrt = int(n ** 0.5)
    if(sqrt*sqrt == n):
        print(n,"is a perfect square of",sqrt)
    else:
        print(n,"is not a perfect square")