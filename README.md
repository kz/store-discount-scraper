# store-discount-scraper

##Overview

This is a Python project (assigned by @wy) to scrape sale items from online stores for exporting to a database. This has been designed in a modular way to make it easy to add/modify modules.

There are three main components:
* main.py - This handles the importing of your modules and prompts the user to select an action.
* mod_*.py - These are modules which scrape and interpret sale data from a single source (web store) and pass the data onto the database. The naming scheme is mod_[domain][tld].py.
* database.py - This handles the creation/modification of databases and importing of sale data into the database. sqlite3 is used as the engine.

### Built With

* Python 3.4.1
    * lxml
    * requests
    * sqlite3

##To-Do

* main.py
    * Create basic user prompt for mod_madecom.
* mod_madecom.py
    * Create regex to index sale pages.
    * Use lxml to scrape sale data.
    * Import data into database.
* database.py
    * Create function to create table and rows.
    * Create table and rows for mod_madecom.
