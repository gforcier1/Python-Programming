# This is a Python script to print a header for Baseball Team Manager

# Print a line of equal signs for visual separation
print("=" * 65)

# Print the header
print("                      Baseball Team Manager\n")
print("This program calculates the batting average for a player based \non the player's official number of at bats and hits.")

# Print another line of equal signs for visual separation
print("=" * 65)

#Get Player inputs of Name, hits, and at bats
name = input("Player's Name:       ")
at_bats = int(input("Official number of at bats:      "))
hits = int(input("Number of hits:        "))

#Calculate batting average
average = hits / at_bats

#Display Name and batting average
print(name + "'s batting average is: " + str(average)) #Convert average to a string
