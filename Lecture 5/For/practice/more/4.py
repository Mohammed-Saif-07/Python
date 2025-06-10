while True:
    choice = int(input("Enter 1 to continue, 0 to stop: "))

    if choice == 1:
        marks = int(input("enter marks: "))

        if(marks >= 90 and marks <= 100):
            print("this is good")
        elif(marks >=60 and marks <=89):
            print("this is also good")
        elif(marks >= 0 and marks <= 59):
            print("this is good as well")
        else:
            print("enter valid no")

    elif choice == 0:
        print("prgram stopped")
        break
    else:
        print("enter valid no")