"""
Pierre Jordan Harrison
22 September 2016
The program is to load a list of items from a csv file, then the user can choose to list the items
hire the items, return the items, or add another items.
The program ended with saving the current situationof all the items into the csv file.
Github link: https://github.com/jc348632/CP1401_Assignment2
"""

# This function for ordering ticket Return or One-Way
def ordering():
    """  The main Function """
    passenger = choosePassenger(username)
    ticketSelection = ticketType()
    if ticketSelection == "Return":
        flight = ticketReturn()
    elif ticketSelection == "One-Way":
        flight = ticketOne()
    classChoice = chooseClass()
    seatType = chooseSeat()
    age = ageInput()
    price = countTotal(ticketSelection, flight, classChoice, seatType) # Count the total fare
    print("Calculating fare . . . ")
    print("Ticket for: " + passenger)
    print(ticketSelection)
    print(flight)
    print(classChoice)
    print(seatType)
    discountedPrice = discountCheck(age, price) # Giving discount for people < 16 year old
    print("Total Price: ${}".format(discountedPrice))
    priceList.append(discountedPrice) # priceList to listed all people's order, so the total could be counted in the (E)xit option
    itemList.append("${:.2f}".format(discountedPrice))

# This is Main Menu function for giving Intruction, Order, and Exit
def mainMenu():
    print("Tropical Airlines Ticket Ordering System")
    print("(I)nstructions")
    print("(O)rder ticket")
    print("(E)xit")
    menuSelection = input()
    menuSelection = menuSelection.upper()
    return menuSelection

# This Function to order ticker for yourself or someone else
def choosePassenger(username):
    while True:
        print(username, " is this ticket for:")
        print("(Y)ou")
        print("(S)omeone else")
        menuChoice = input()
        menuChoice = menuChoice.upper()
        if  menuChoice == "Y":
            passenger = username
            break
        elif menuChoice == "S":
            passenger = input("Please enter the name of the person travelling")
            break
        else:
            print("Invalid menu Choice")
    return passenger

# This function for giving options for Return and On-Way ticket
def ticketType():
    while True:
        print("Is this a")
        print("(R)eturn trip")
        print("(O)ne-Way")
        ticketSelection = input()
        ticketSelection = ticketSelection.upper()
        if ticketSelection == "R":
            typeChoice = "Return"
            break
        elif ticketSelection == "O":
            typeChoice = "One-Way"
            break
        else:
            print("Invalid menu Choice")
    return typeChoice

# This function to run the Return ticket function
def ticketReturn():
    while True:
        print("Please select the destination for your return trip. Fare prices are listed below.")
        print("(C)airns  - $400")
        print("(S)ydney  - $575")
        print("(P)erth  - $700")
        ticketTypes = input()
        ticketTypes = ticketTypes.upper()
        if ticketTypes == "C":
            flight = "Cairns"
            break
        elif ticketTypes == "S":
            flight = "Sydney"
            break
        elif ticketTypes == "P":
            flight = "Perth"
            break
        else:
            print("Invalid menu Choice")
    return flight

# This function is to run the One-Way ticket function
def ticketOne():
    while True:
        print("Please select the destination for your One-Way trip. Fare prices are listed below.")
        print("(C)airns  - $250")
        print("(S)ydney  - $420")
        print("(P)erth  - $510")
        ticketSelecetions = input()
        ticketSelecetions = ticketSelecetions.upper()
        if ticketSelecetions == "C":
            flight = "Cairns"
            break
        elif ticketSelecetions == "S":
            flight = "Sydney"
            break
        elif ticketSelecetions == "P":
            flight = "Perth"
            break
        else:
            print("Invalid menu Choice")
    return flight

# This function for Choosing type of class fare
def chooseClass():
    while True:
        print("Please choose the type of fare. Fees are displayed below and are in addition to the basic fare. Please note choosing Frugal fare means you will not be offered a seat choice, it will be assigned to the ticketholder at travel time.")
        print("(B)usiness  – $275")
        print("(E)conomy  – $25")
        print("(F)rugal  – $0")
        classSelection = input()
        classSelection = classSelection.upper()
        if classSelection == "B":
            classChoice = "Business"
            break
        elif classSelection == "E":
            classChoice = "Economy"
            break
        elif classSelection == "F":
            classChoice = "Frugal"
            break
        else:
            print("Invalid menu choice")
    return classChoice

# This function to choosing seat type
def chooseSeat():
    while True:
        print("Please choose the seat type.  Choosing the middle seat will deduct 25 from the total fare.")
        print("(W)indow  +  $75")
        print("(A)isle  + $50")
        print("(M)iddle  - $25")
        seatSelection = input()
        seatSelection = seatSelection.upper()
        if seatSelection == "W":
            seatType = "Window"
            break
        if seatSelection == "A":
            seatType = "Aisle"
            break
        if seatSelection == "M":
            seatType = "Middle"
            break
        else:
            print("Invalid Selection")
    return seatType

# This funciton is to input passanger age and there is no negative number
def ageInput():
    while True:
        passangerAge = int(input("How old is the person travelling. Travellers under 16 years old will receive a 50% discount for the child fare."))
        if passangerAge<0:
            print("Please enter a positive number")
        else:
            break
    return passangerAge

# This function is giving discount for poeple < 16 years old
def discountCheck(age, price):
    """ The discount function """
    if age < 16: # Age < 16 can get discount 50% off
        price = price / 2
        print("Age: " + str(age) + " (Eligible for child ticket)")
    else:
        print("Age: " + str(age) + "(Not eligible for child ticket)")
    return price

# This function is to count the total Price of the ticket
def countTotal(ticketSelection, flight, classChoice, seatType):
    """  To calculate the total from ticketSelection, flight, classChoice, and seatType """
    if ticketSelection == "Return":
        if flight == "Cairns":
            price = 400
        elif flight == "Sydney":
            price = 575
        elif flight == "Perth":
            price = 700
    elif ticketSelection == "One-Way":
        if flight == "Cairns":
            price = 250
        elif flight == "Sydney":
            price = 420
        elif flight == "Perth":
            price = 510
    if classChoice == "Business":
        price += 275
    elif classChoice == "Economy":
        price += 25
    elif classChoice == "Frugal":
        price = price
    if seatType == "Window":
        price +=75
    elif seatType == "Aisle":
        price += 50
    elif seatType == "Middle":
        price -= 25
    return price

# This is the command to count all the total price for more than 1 person using list command
itemList = []
priceList = []
print("What is your name?")
username = input()
print("Welcome ", username)
menuSelection = mainMenu()
while menuSelection != "E":
    if menuSelection == "I":
        print("Thank you for choosing Tropical Airlines for your air travel needs. You will be asked questions regarding what type of ticket you would like to purchase as well as destination information. We also offer 50% discounted fares for children.")
    elif menuSelection == "O":
        ordering()
    else:
        print("Invalid menu choice")
    menuSelection = mainMenu()
print("{} your order: {} Your final total is: ${} Thank you for visiting Tropical Airlines".format(username, " and ".join(itemList), sum(priceList)))
