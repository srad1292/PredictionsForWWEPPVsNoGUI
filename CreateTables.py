import sqlite3

#name of sqlite database file
sqlite_file = 'ppv_predictions_db.sqlite'
#name of tables to create
table_wrestlers = 'wrestlers'
table_matches = 'matches'
table_participants = 'participants'
table_winners = 'winners'
table_losers = 'losers'
table_draws = 'draws'
table_other = 'other'
table_shows = 'shows


conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#Create the wrestlers table
cursor.execute("""CREATE TABLE wrestlers
                  (id INTEGER PRIMARY KEY, name TEXT NOT NULL) 
               """)


#Create the shows table
cursor.execute("""CREATE TABLE shows
                  (id INTEGER PRIMARY KEY, name TEXT NOT NULL, year INTEGER NOT NULL,
                   month INTEGER NOT NULL, day INTEGER NOT NULL) 
               """)


#Create the matches table
cursor.execute("""CREATE TABLE matches
                  (id INTEGER PRIMARY KEY, result INTEGER NOT NULL,
                   show_id INTEGER, FOREIGN KEY(show_id) REFERENCES shows(id)) 
               """)

#Create the participants table
cursor.execute("""CREATE TABLE participants
                  (wrestler_id INTEGER, match_id INTEGER,
                   FOREIGN KEY(wrestler_id) REFERENCES wrestlers(id),
                   FOREIGN KEY(match_id) REFERENCES matches(id),
                   PRIMARY KEY (wrestler_id, match_id))
               """)

#Create the winners table
cursor.execute("""CREATE TABLE winners
                  (wrestle_id INTEGER, match_id INTEGER,
                   FOREIGN KEY(wrestler_id) REFERENCES wrestlers(id),
                   FOREIGN KEY(match_id) REFERENCES matches(id),
                   PRIMARY KEY (wrestler_id, match_id))
               """)

#Create the losers table
cursor.execute("""CREATE TABLE losers
                  (wrestle_id INTEGER, match_id INTEGER,
                   FOREIGN KEY(wrestler_id) REFERENCES wrestlers(id),
                   FOREIGN KEY(match_id) REFERENCES matches(id),
                   PRIMARY KEY (wrestler_id, match_id)) 
               """)

#Create the draws table
cursor.execute("""CREATE TABLE draws
                  (wrestle_id INTEGER, match_id INTEGER,
                   FOREIGN KEY(wrestler_id) REFERENCES wrestlers(id),
                   FOREIGN KEY(match_id) REFERENCES matches(id),
                   PRIMARY KEY (wrestler_id, match_id))
               """)

#Create the other table
cursor.execute("""CREATE TABLE other
                  (wrestle_id INTEGER, match_id INTEGER,
                   FOREIGN KEY(wrestler_id) REFERENCES wrestlers(id),
                   FOREIGN KEY(match_id) REFERENCES matches(id),
                   PRIMARY KEY (wrestler_id, match_id))
               """)

