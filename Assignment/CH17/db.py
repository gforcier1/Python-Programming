import csv
import sqlite3
from contextlib import closing
from objects import Player,Lineup

FILENAME = "players.csv"

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "player_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_player(row):
    return Player(row["playerID"], row["batOrder"], row["firstName"], row["lastName"],
                  row["position"], row["atBats"], row["hits"])

def get_players():
    try:
        sql = '''SELECT playerID, batOrder, firstName,
                        lastName, position, atBats, hits
                 FROM Player'''
        with closing(conn.cursor()) as c:
            c.execute(sql)
            rows = c.fetchall()

            players = Lineup()
            for row in rows:
                player = make_player(row)
                players.add(player)

            return players

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
                  

def get_player(id):
    sql = '''SELECT playerID, batOrder, firstName,
                    lastName, position, atBats, hits
             FROM Player
             WHERE playerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (id,))
        row = c.fetchone()
        if row:
            return make_player(row)
        return None

def add_player(player):
    sql = '''INSERT INTO Player(playerID, batOrder, firstName, lastName, position, atBats, hits)
             VALUES (?, ?, ?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (player.playerID, player.batOrder, player.firstName, player.lastName,
                        player.position, player.atBats, player.hits))
    conn.commit()

def delete_player(player):
    sql = '''DELETE FROM Player
             WHERE playerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (player,))
    conn.commit()

def update_bat_order(lineup):
    for num, player in enumerate(lineup, start=1):
        player.batOrder = num
        sql = '''UPDATE Player
                 SET batOrder = ?
                 WHERE playerID = ?'''
        with closing(conn.cursor()) as c:
            c.execute(sql, (player.batOrder, player.playerID))
    conn.commit()
    

def update_player(player):
    sql = '''UPDATE Player
             SET batOrder = ?, firstName = ?, lastName = ?,
                 position = ?, atBats = ?, hits = ?
             WHERE playerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (player.batOrder, player.firstName, player.lastName,
                        player.position, player.atBats, player.hits, player.playerID))
    conn.commit()
