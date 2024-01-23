import requests
from bs4 import BeautifulSoup

def scrape_cryptocurrency_data(cryptocurrency):
    url = f"https://coinmarketcap.com/currencies/{cryptocurrency}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting the price
        price = soup.find('span', class_='sc-f70bb44c-0 jxpCgO base-text').get_text()        

        return {
            'name': cryptocurrency,
            'price': price
        }

    else:
        return {'error': 'Failed to retrieve data'}

cryptocurrencies = ['bitcoin', 'ethereum', 'ripple', 'litecoin', 'cardano', 'solana', 'polkadot', 'dogecoin', 'chainlink', 'stellar', 'uniswap', 'bnb', 'tether', 'bitcoin-cash', 'tron']
for crypto in cryptocurrencies:
    data = scrape_cryptocurrency_data(crypto)
    print(data)
