# store-discount-scraper

##Overview

This is a Python project (assigned by @wy) to scrape sale items from online stores for exporting to a database. This has been designed in a modular way to make it easy to add/modify modules.

There are three main components:
* main.py - This handles the importing of your modules and prompts the user to select an action.
* main_database.py - This handles the creation/modification of databases and importing of sale data into the database. sqlite3 is used as the engine.
* mod_*.py - These are modules which scrape and interpret sale data from a single source (web store) and pass the data onto the database. The naming scheme is mod_[domain][tld].py.

### Built With

* Python 3.4.1
    * lxml
    * requests
    * sqlite3