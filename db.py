import sqlite3

conn = sqlite3.connect('games.db')
cursor = conn.cursor()
create_table = "CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY, name text, platform foreign key, price real, description text, release_date date, category foreign key, players int)"
cursor.execute(create_table)
create_table = "CREATE TABLE IF NOT EXISTS platforms (id INTEGER PRIMARY KEY, name text, release_date date, price_first_release real)"
cursor.execute(create_table)
create_table = "CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY, name text)"
cursor.execute(create_table)
conn.commit()
conn.close()