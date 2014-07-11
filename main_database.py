# Import database modules.	
import sqlite3
import os

def create_table(table_name, table_columns):
    # Opens the database connection.
    db = sqlite3.connect(r'C:\Users\Kelvin\Dropbox\Projects\Git Projects\store-discount-scraper\database.sqlite3')
    cur = db.cursor()
    
    # Creates the table as specified if it doesn't exist.
    sql = 'CREATE TABLE IF NOT EXISTS {0} ('.format(table_name)
    for table_column in table_columns:
        sql = sql + table_column[0] + ' ' + table_column[1] + ', '
    sql = sql[:-2] + ')'
    cur.execute(sql)
    
    # Closes the database connection.
    db.close() 

def madecom(products):
    # Opens the database connection.
    db = sqlite3.connect(r'C:\Users\Kelvin\Dropbox\Projects\Git Projects\store-discount-scraper\database.sqlite3')
    cur = db.cursor()
    
    for product in products:
        cur.execute("INSERT OR IGNORE INTO madecom VALUES (?, ?, ?, ?, ?, ?, ?)", (product[0],product[1],product[2],product[3],int(product[4]),product[5],product[6]))
    
    # Closes the database connection.
    db.close() 