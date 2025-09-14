import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "cricbuzz.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS players (player_id INTEGER PRIMARY KEY, full_name TEXT, country TEXT, playing_role TEXT);
CREATE TABLE IF NOT EXISTS matches (match_id INTEGER PRIMARY KEY, match_desc TEXT, team1_id INTEGER, team2_id INTEGER, venue_id INTEGER, match_date DATE, winner_id INTEGER);
CREATE TABLE IF NOT EXISTS teams (team_id INTEGER PRIMARY KEY, team_name TEXT, country TEXT);
CREATE TABLE IF NOT EXISTS venues (venue_id INTEGER PRIMARY KEY, venue_name TEXT, city TEXT, capacity INTEGER);
CREATE TABLE IF NOT EXISTS player_stats (stat_id INTEGER PRIMARY KEY, player_id INTEGER, match_id INTEGER, format TEXT, runs_scored INTEGER, wickets_taken INTEGER, batting_average REAL);
CREATE TABLE IF NOT EXISTS batting_partnerships (partnership_id INTEGER PRIMARY KEY, player1 TEXT, player2 TEXT, runs INTEGER, innings INTEGER);

INSERT INTO players (full_name, country, playing_role) VALUES ('Virat Kohli', 'India', 'Batsman');
INSERT INTO teams (team_name, country) VALUES ('India', 'India'), ('England', 'England');
INSERT INTO venues (venue_name, city, capacity) VALUES ('Wankhede Stadium', 'Mumbai', 33000);
INSERT INTO matches (match_desc, team1_id, team2_id, venue_id, match_date, winner_id) VALUES ('India vs England', 1, 2, 1, '2025-09-10', 1);
INSERT INTO player_stats (player_id, match_id, format, runs_scored, wickets_taken, batting_average) VALUES (1, 1, 'ODI', 75, 0, 55.3);
INSERT INTO batting_partnerships (player1, player2, runs, innings) VALUES ('Virat Kohli', 'Rohit Sharma', 150, 1);
""")

conn.commit()
conn.close()

print("Sample database created successfully at", db_path)

