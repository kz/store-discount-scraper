# Import database modules.	
import sqlite3

# TODO: Function to handle database.

# Opens the database connection.
db = sqlite3.connect('data/database.sqlite3')
# Closes the database connection.
db.close()