import sqlite3
import os
from sys import argv
from database import initialize_db, add_auction, list_auctions, update_auction_price
from views import display_auction_table
from fetcher import fetch_auction_price
from time import sleep
from dotenv import load_dotenv


def update_auctions(auctions):
    for auction in auctions:
        new_price = fetch_auction_price(auction[1])
        print(f'New price for {auction[1]} is {new_price}.')
        update_auction_price(connection, auction[0], new_price)


try:
    load_dotenv(verbose=True)
    print(f'Baza: {os.getenv("DB_NAME")}')
    connection = sqlite3.connect(os.getenv('DB_NAME'))
    if len(argv) > 1:
        if argv[1] == 'startup':
            # python main.py startup
            initialize_db(connection)

        elif argv[1] == 'add':
            # python main.py add <link do aukcji>
            add_auction(connection, argv[2])

        elif argv[1] == 'update':
            auctions = list_auctions(connection)
            update_auctions(auctions)
        elif argv[1] == 'update-daemon':
            while True:
                auctions = list_auctions(connection)
                update_auctions(auctions)
                print(display_auction_table(list_auctions(connection)))
                sleep(60)
    else:
        # list all auctions
        print(display_auction_table(list_auctions(connection)))

except Exception as error:
    print(error)
