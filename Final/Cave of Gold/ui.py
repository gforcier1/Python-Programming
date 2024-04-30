import db
import random
from lib import weapons, locations

def display_separator():
    print("*" * 70)

def game_separator():
    print("-" * 60)

def display_stars():
    print("*" * 70)

def display_title():
    print("                             Cave of Gold")

def display_path_choices():
    print("...***---***---***...***---Mori...***---***---***---***...")
    print("...***---***---***...***---Latere...***---***---***---***...")
    print("...***---***---***...***---Aurum...***---***---***---***...")

def main():
    #Title
    display_separator()
    display_title()
    display_separator()

    #Database connection and table creation
    db.connect()
    db.create_tables()

    #Create weapons and locations from db and lib
    db.create_weapons(weapons())
    db.create_locations(locations())

    #Create character
    name = input("Enter your name, Challenger: ")
    new_gamer_id = db.create_character(name)
    #retrieve character data
    if new_gamer_id:
        Player = db.get_character(new_gamer_id)

        # Display character data
        if Player:
            print("Character created successfully:")
            game_separator()
            print(Player.getStart)
            game_separator()
            print(Player.getWeapon)
            game_separator()
        else:
            print("Failed to retrieve character data.")
    else:
        print("Failed to create character.")

    #Begin Loop
    while Player.is_alive():
        #Prompt choice of location
        display_path_choices()
        game_separator()
        choice = input("Choose a fortune and be taken away: ")

        if choice.lower() in ["mori", "latere", "aurum"]:
            # Update the player's location based on their choice. Random location chosen
            new_location = db.get_random_location()
            Player.move_to(new_location[0], new_location[1], new_location[2], new_location[3])
            game_separator()
            print(Player.getLocation)
        else:
            print("Wrong. You Must Choose.")

        #enemy encounter
        game_separator()
        print(Player.getEnemy)
        game_separator()
        
        #Check if weapon damage is less than enemy health. defeat enemy is not.
        #Give player chance to flee if encounter failed
        if Player.weapon_damage < Player.enemy_health:
            
            flee_success = random.choice([True, False])
            print(f"Your weapon is too weak to defeat them.")
            print(f"You attempt to flee")
            game_separator()

            if flee_success:
                print("You manage to escape from the enemy!")
            else:
                print("Your attempt to flee fails.")
                print("The enemy clobbers you while you hasten away.")
                Player.take_damage()
        else:
            print(f"You've defeated the enemy!")


        game_separator()
        #Status display before next choice
        print(Player.getStatus)
        game_separator()
        
        if not Player.is_alive():
            print(f"{Player.name} has been defeated!")
            display_stars()
            print(Player.getDefeat)
            display_stars()


main()
