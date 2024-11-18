import requests
from bs4 import BeautifulSoup

response = requests.get("https://coinmarketcap.com/")
soup = BeautifulSoup(response.text, features="html.parser")

coins_names = soup.find_all("p", {"class":"sc-65e7f566-0 iPbTJf coin-item-name"})
coins_symbols = soup.find_all("p", {"class":"sc-1eb5slv-0 gGIpIK coin-item-symbol"})
coins_values = soup.find_all("div", {"class":"sc-b3fc6b7-0 dzgUIj"})

for i in range(0, len(coins_symbols)):
    print(f"{coins_names[i].text} ({coins_symbols[i].text}) {coins_values[i].text}")

print(coins_names)
print(coins_symbols)