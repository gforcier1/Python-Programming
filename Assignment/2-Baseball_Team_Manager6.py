#Define positions in a tuple
positions_tuple = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')

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
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program\n")
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")


#function to call command menu
def command_menu():
    separator()
    title()
    menu()
    separator()

#function for calculating batting average
def get_batting_average(hits, at_bats):
     average = round(hits / at_bats, 3)
     return average

#function to add players
def add_player(players):
    name = input("Name: ")
    position = get_player_position()
    at_bats = get_at_bats()
    hits = get_hits(at_bats)
    player = {'Name': name, 'Position': position, 'At Bats': at_bats, 'Hits': hits}
    players.append(player)
    print(f"{name} added.")

#function to get player positions
def get_player_position():
    position = input("Position: ").upper()
    while position not in positions_tuple:
        print("Invalid position. Please enter valid position.")
        position = input("Position: ").upper()
    return position
    
#function to get at bats
def get_at_bats():
    while True:
        at_bats = int(input("At bats: "))
        if at_bats < 0:
            print("Invalid entry. Please enter value greater than 0.")
        else:
            return at_bats

#function to get hits
def get_hits(at_bats):
    while True:
        hits = int(input("Hits: "))
        if hits < 0 or hits > at_bats:        
            print(f"Invalid entry. Must be from 0 to {at_bats}.")
        else:
            return hits

#function to get lineup number
def get_lineup_number(players, prompt):
    lineup_number = int(input(prompt))
    return lineup_number

#function to delete players
def delete_player(players):
    lineup_number = get_lineup_number(players, "Enter the lineup number of the player to delete: ")
    if lineup_number is not None:
        deleted_player = players.pop(lineup_number - 1)
        print(f"{deleted_player['Name']} deleted successfully.")
        
#function to move players
def move_player(players):
    lineup_number = get_lineup_number(players, "Enter the lineup number of the player to move: ")
    if lineup_number is not None:
        new_position = get_player_position()
        players[lineup_number - 1]['Position'] = new_position
        print("Player moved successfully.")

#function to edit player position
def edit_player_position(players):
    lineup_number = get_lineup_number(players, "Enter the lineup number of the player to edit position: ")
    if lineup_number is not None:
        new_position = get_player_position()
        players[lineup_number - 1]['Position'] = new_position
        print("Player position edited successfully.")

#function to edit players stats
def edit_player_stats(players):
    lineup_number = get_lineup_number(players, "Enter the lineup number of the player to edit stats: ")
    if lineup_number is not None:
        new_at_bats = get_at_bats()
        new_hits = get_hits(new_at_bats)
        players[lineup_number - 1]['At Bats'] = new_at_bats
        players[lineup_number - 1]['Hits'] = new_hits
        print("Player stats edited successfully.")

#function to display lineup
def display_lineup(players):
    separator()
    print("LINEUP")
    print(f"{'No': <5}{'Name': <20}{'Position': <5}{'At Bats': <10}{'Hits': <10}{'Batting Avg': <15}")
    for i, player in enumerate(players, start=1):
        at_bats = player['At Bats']
        hits = player['Hits']
        batting_average = get_batting_average(hits, at_bats)

        print(f"{i: <5}{player['Name']: <20}{player['Position']: <5}{at_bats: <10}{hits: <10}{batting_average: <15.3f}")
    separator()
    
#main function
def main():

    #Initialize players list
    players = []

    #call command menu
    command_menu()

    #start a loop to handle commands
    while True:
        command = int(input("Menu Option: "))
        if command == 1:
            display_lineup(players)
        elif command == 2:
            add_player(players)
        elif command == 3:
            delete_player(players)
        elif command == 4:
            move_player(players)
        elif command == 5:
            edit_player_position(players)
        elif command == 6:
            edit_players_stats(players)
        elif command == 7:
            print("Bye.")
            break
        else:
            print("Invalid command. Please try again.")
            command_menu()

#Call main function    
main()
