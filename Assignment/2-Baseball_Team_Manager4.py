#Header function
def separator():
    # Print a line of equal signs for visual separation
    print("=" * 65)

#function to print a line for the title
def title():
    print("                      Baseball Team Manager\n")

#function to print the menu options
def menu():
    print("MENU OPTIONS")
    print("1 - Calculate batting average")
    print("2 - Exit Program")

#function for calculating batting average
def batting_average(hits, at_bats):
     average = round(hits / at_bats, 3)
     return average

#main function
def main():
    separator()
    title()
    menu()
    separator()

    while True:
        #input for menu option
        option = int(input("Menu option: "))

        if option == 1:
            print("Calculating batting average...")

            #inputs of hits and at bats
            at_bats = int(input("Official number of at bats: "))
            hits = int(input("Number of hits: "))

            #Call batting average function and storing in average
            average = batting_average(hits, at_bats)

            #Display batting average
            print("Batting average:", average)
        elif option == 2:
            print("Exiting program. Bye!")
            break
        else:
            print("Invalid menu option. Please enter 1 or 2.")

#Call main function    
main()
