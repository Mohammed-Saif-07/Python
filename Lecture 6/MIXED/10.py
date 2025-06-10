pcount = 0
ncount = 0
zcount = 0

while True:
    print("Enter 1 to continue or 0 to stop")

    choice = int(input())
    if choice == 0:
        print("program stopped")
        break
    elif choice == 1:
        num = int(input())

        if num > 0:
            pcount+=1
        elif num < 0:
            ncount+=1
        else:
            zcount+=1
        
    else:
        print("invalid entry")

print("positive",pcount)
print("negative",ncount)
print("zeroes",zcount)
