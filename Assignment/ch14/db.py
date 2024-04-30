import csv
from objects import Player

FILENAME = "players.csv"

def read_players():
    players = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            # convert hits and at bats from strings to ints
            row[3] = int(row[3]) 
            row[4] = int(row[4])
            player = Player(firstName=row[0], lastName=row[1], position=row[2], at_bats=row[3], hits=row[4])
            players.append(player)
    return players

def write_players(players):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows([[player.firstName, player.lastName, player.position, player.at_bats, player.hits] for player in players])

