from terminaltables import AsciiTable


def display_auction_table(auctions):
    table_data = [
        [
            'Id',
            'Adres url',
            'Cena stara',
            'Cena nowa',
            'Aktualizacja'
        ]
    ]

    table_data += auctions
    return AsciiTable(table_data).table