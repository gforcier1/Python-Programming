import sqlite3
import random
from contextlib import closing
from lib import weapons, locations
from objects import Gamer

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "game_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def create_tables():
    #Create character table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS char (
            gamer_id    INTEGER  PRIMARY KEY AUTOINCREMENT,
            name        TEXT       NOT NULL,
            health      INTEGER    NOT NULL,
            weapon_id   INTEGER    NOT NULL,
            location_id INTEGER    NOT NULL
        )
    ''')
    #Create weapons table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS wep (
            weapon_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT      NOT NULL,
            damage INTEGER NOT NULL
        )
    ''')
    #Create locations table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS loc (
            location_id INTEGER  PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            enemyHealth INTEGER NOT NULL,
            gold        INTEGER NOT NULL
        )
    ''')

    # Create leaderboard table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS leaderboard (
            player_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gold INTEGER NOT NULL,
            weapon_name TEXT NOT NULL
        )
    ''')

    conn.commit()

#Function to create character
def create_character(name):
    health = 40
    weapon_id = random.randint(1, 10)
    location_id = 1
    conn.execute('''
        INSERT INTO char (
            name, health, weapon_id, location_id
            ) VALUES (?, ?, ?, ?)
            ''',
            (name, health, weapon_id, location_id))

    conn.commit()

    cursor = conn.execute('''SELECT gamer_id
                             FROM char
                             WHERE name = ?
                             ''',
                                (name,))
    new_gamer_id = cursor.fetchone()['gamer_id']
    return new_gamer_id

#Function to retreive char info
def get_character(new_gamer_id):
    try:
        sql = '''SELECT char.gamer_id, char.name, char.health, char.weapon_id, char.location_id,
                        wep.name, wep.damage, loc.name, loc.enemyHealth, loc.gold
                 FROM char
                 JOIN wep ON char.weapon_id = wep.weapon_id
                 JOIN loc ON char.location_id = loc.location_id
                 WHERE char.gamer_id = ?
                 '''
        with closing(conn.cursor()) as c:
            c.execute(sql, (new_gamer_id,))
            rows = c.fetchone()

            if rows:
                gamer_id, char_name, health, weapon_id, location_id, weapon_name, weapon_damage, location_name, enemy_health, gold = rows
                return Gamer(gamer_id, char_name, health, weapon_id, location_id, weapon_name, weapon_damage, location_name, enemy_health, gold)
            else:
                print("Character not found")
                return None
    except Exception as e:
        print(f"Get Character Error: {e}")
        return None

# Function to create weapons
def create_weapons(weapons):
    for weapon in weapons:
        name, damage = weapon
        
        cursor = conn.execute('''SELECT *
                              FROM wep
                              WHERE name = ? AND damage = ?
                           ''',
                              (name, damage))
        existing_weapon = cursor.fetchone()

        if not existing_weapon:
            conn.execute('''
                INSERT INTO wep (
                name, damage
                ) VALUES (?, ?)
                ''',
                (name, damage))

    conn.commit()

# Function to create locations
def create_locations(locations):
    for location in locations:
        name, enemy_health, gold = location

        cursor = conn.execute('''SELECT *
                                 FROM loc
                                 WHERE name = ? AND enemyHealth = ? AND gold = ?
                                 ''',
                                    (name, enemy_health, gold))
        existing_location = cursor.fetchone()

        if not existing_location:
            conn.execute('''
                INSERT INTO loc (
                name, enemyHealth, gold
                ) VALUES (?, ?, ?)
                ''',
                (name, enemy_health, gold))

    conn.commit()

#get all locations so they can be chosen at random
def get_all_locations():
    try:
        cursor = conn.execute("SELECT * FROM loc")
        locations = cursor.fetchall()

        return locations
    except Exception as e:
        print(f"Error getting locations: {e}")
        return []

#Use get all locations result to choose random location
def get_random_location():
    all_locations = get_all_locations()

    # If there are no locations, return a default tuple
    if not all_locations:
        return (0, 0, 0, 0)

    # Get a random location tuple from the list
    return random.choice(all_locations)

#Leaderboard functionality
def insert_into_leaderboard(name, gold, weapon_name):
    conn.execute('''
        INSERT INTO leaderboard (name, gold, weapon_name)
        VALUES (?, ?, ?)
    ''', (name, gold, weapon_name))
    conn.commit()

def get_leaderboard():
    with closing(conn.cursor()) as c:
        c.execute('''
            SELECT name, gold, weapon_name
            FROM leaderboard
            ORDER BY gold DESC
        ''')
        rows = c.fetchall()
        return rows


