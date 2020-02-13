def initialize_db(connection):
    print('Re-creating tables...')

    sql = """ CREATE TABLE auctions (
        id integer PRIMARY KEY AUTOINCREMENT,
        url text NOT NULL,
        price_old float,
        price float,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

    cursor = connection.cursor()
    cursor.execute(sql)


def add_auction(connection, url):
    print('Adding new auction...')

    sql = 'INSERT INTO auctions(url) VALUES(?)'
    cursor = connection.cursor()
    cursor.execute(sql, (url,))
    connection.commit()

def update_auction_price(connection, auction_id, new_price):
    print('Updating auction\'s price...')

    sql = 'UPDATE auctions SET price=?, price_old=price, updated_at=CURRENT_TIMESTAMP WHERE id=? AND (price<>? or price is NULL)'
    cursor = connection.cursor()
    cursor.execute(sql, (new_price, auction_id, new_price))
    connection.commit()


def list_auctions(connection):
    sql = 'SELECT * FROM auctions'
    cursor = connection.cursor()
    cursor.execute(sql)

    return cursor.fetchall()



