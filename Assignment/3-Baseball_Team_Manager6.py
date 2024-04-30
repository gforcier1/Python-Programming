import db

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

def add_player(players):
    name = input("Name: ").title()
    position = get_player_position()
    at_bats = get_at_bats()
    hits = get_hits(at_bats)
    
    player = []
    player.append(name)
    player.append(position)
    player.append(at_bats)
    player.append(hits)
    players.append(player)
    print(f"{name} was added.\n")

def get_player_position():
    while True:
        position = input("Position: ").upper()
        if position in POSITIONS:
            return position
        else:
            print("Invalid position. Try again.")
            display_positions()

def get_at_bats():
    while True:
        at_bats = int(input("At bats: "))
        if at_bats < 0 or at_bats > 10000:    
            print("Invalid entry. Must be from 0 to 10,000.")
        else:
            return at_bats

def get_hits(at_bats):
    while True:
        hits = int(input("Hits: "))
        if hits < 0 or hits > at_bats:        
            print(f"Invalid entry. Must be from 0 to {at_bats}.")
        else:
            return hits

def get_lineup_number(players, prompt):
    while True:
        number = int(input(prompt))
        if number < 1 or number > len(players):
            print("Invalid player number. Please try again.")
        else:
            return number

def delete_player(players):
    number = get_lineup_number(players, "Number: ")
    player = players.pop(number-1)
    print(f"{player[0]} was deleted.\n")

def move_player(players):
    old_number = get_lineup_number(players, "Current lineup number: ") 
    print(f"{players[old_number-1][0]} was selected.")
    new_number = get_lineup_number(players, "New lineup number: ")

    player = players.pop(old_number-1)
    players.insert(new_number-1, player)
    print(f"{player[0]} was moved.\n")

def edit_player_position(players):
    number = get_lineup_number(players, "Lineup number: ")
    player = players[number-1]
    print(f"You selected {player[0]} POS={player[1]}")
    
    position = get_player_position()
    player[1] = position
    print(f"{player[0]} was updated.\n")

def edit_player_stats(players):
    number = get_lineup_number(players, "Lineup number: ")
    player = players[number-1]
    print(f"You selected {player[0]} AB={player[2]} H={player[3]}")
    
    at_bats = get_at_bats()
    hits = get_hits(at_bats)
    player[2] = at_bats
    player[3] = hits
    print(f"{player[0]} was updated.\n")

def display_lineup(players):
    if players == None:
        print("There are currently no players in the lineup.")        
    else:
        print("\tPlayer\t\tPOS\tAB\tH\tAVG")
        print("----------------------------------------------------------------")
        for i, player in enumerate(players, start=1):
            name = player[0]
            position = player[1]
            at_bats = player[2]
            hits = player[3]
            avg = get_batting_avg(at_bats, hits)
            print("Batting average:","{:.3f}".format(round(avg, 3)))
            print(f"{i}\t{name}\t\t{position}\t{at_bats}\t{hits}\t","{:.3f}".format(round(avg, 3)))
    print()    

def get_batting_avg(at_bats, hits):
    avg = hits / at_bats
    return round(avg, 3)

def display_separator():
    print("================================================================")

def display_title():
    print("                   Baseball Team Manager")

def display_menu():
    print("MENU OPTIONS")
    print("1 – Display lineup")
    print("2 – Add player")
    print("3 – Remove player")
    print("4 – Move player")
    print("5 – Edit player position")
    print("6 – Edit player stats")
    print("7 - Exit program")
    print()

def display_positions():
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")

def main():
    display_separator()
    display_title()
    display_menu()
    display_positions()
    display_separator()

    players = []
    while True:
        option = int(input("Menu option: "))
            
        if option == 1:
            display_lineup(players)
        elif option == 2:
            add_player(players)
        elif option == 3:
            delete_player(players)
        elif option == 4:
            move_player(players)
        elif option == 5:
            edit_player_position(players)
        elif option == 6:
            edit_player_stats(players)
        elif option == 7:
            print("Bye!")
            break
        else:
            print("Not a valid option. Please try again.\n")
            display_menu()

if __name__ == "__main__":
    main()
