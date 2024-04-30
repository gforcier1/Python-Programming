#!/usr/bin/env python3

import csv
import baseball_team

PLAYERS = "players.csv"

def read_players():
    players = []
    with open(PLAYERS, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            position = row[1]
            at_bats = int(row[2])
            hits = int(row[3])
            
            player_data = (name, position, at_bats, hits)
            players.append(player_data)
    return players


def write_players(players):
    with open(PLAYERS, newline="") as file:
        writer = csv.writer(file)
        writer.writerows(players)

