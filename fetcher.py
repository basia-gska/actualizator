from urllib.request import urlopen
from bs4 import BeautifulSoup


def fetch_auction_price(url):
    with urlopen(url) as request:
        content = request.read().decode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        element = soup.find('meta', itemprop='price')
        return float(element.get('content'))

