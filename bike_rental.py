print("*********** BIKE RENTAL SYSTEM **********************")
print("1. Display available bikes")
print("2. Rent some bikes (Cost per bike = 100/-)")
print("3. Exit")

bikes = 100
while True:
    
    num = int(input("Enter your choice :"))

    if num == 1:
        print(f"The total bikes available are {bikes}.")
    elif num == 2:
        rent = int(input("How many bikes do you want? :"))
        if rent > bikes:
            print(f"The available bikes are only {bikes}.")
            rent = int(input("How many bikes do you want? :"))
        bikes = bikes - rent
        cost = rent*100
        print(f"So you want {rent} bikes So accordingly the total cost of rent becomes {cost}")
    elif num==3:
        exit()
    else:
        print("Invalid choice")
