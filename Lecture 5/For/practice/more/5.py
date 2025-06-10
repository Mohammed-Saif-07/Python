# Create a menu-driven program where the user can choose to either input the temperature of a day in Celsius or exit the program.

# If the user enters 1, ask them to input a temperature.

# If the temperature is above 40°C, print "It's too hot!"

# If the temperature is between 20°C and 40°C, print "The weather is pleasant."

# If the temperature is below 20°C, print "It's cold today."

# If the user enters 0, stop the program.

while True:
    entry = int(input("Enter 1 to continue, 0 to stop: "))

    if entry == 1:
        temp = int(input("Enter temperature: "))

        if(temp >= 40):
            print("it is too hot")
        elif(temp >= 20 and temp <= 39):
            print("weather is pleasant today")
        elif(temp < 20):
            print("it is cold today")
        else:
            print("enter valid no")
    
    elif entry == 0:
        print("program stopped")
        break
    else:
        print("enter valid no")