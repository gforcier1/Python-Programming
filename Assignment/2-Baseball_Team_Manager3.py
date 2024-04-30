# Print a line of equal signs for visual separation
print("=" * 65)

# Print the header
print("                      Baseball Team Manager\n")
print("MENU OPTIONS")
print("1 - Calculate batting average")
print("2 - Exit Program")

# Print another line of equal signs for visual separation
print("=" * 65)

#Input for menu option
option = int(input("Menu option: "))

#If statement checking if menu option was valid
if option not in [1,2]:
    print("Error: Invalid menu option. Please enter 1 or 2")
else:

    #Loop for calculating batting average
    while option == 1:
        #Display Calculating for fun
        print("Calculate batting average...")
    
        #Get inputs of  hits, and at bats
        at_bats = int(input("Official number of at bats: "))
        hits = int(input("Number of hits: "))

        #Calculate average and round to 3 decimals
        average = round(hits / at_bats, 3)

        #Display batting average
        print("Batting average: ", average)

        #Ask for another calculation or exit
        option = int(input("Menu option: "))

print("Bye!")
