import requests
from bs4 import BeautifulSoup

response = requests.get('https://httpbin.org/get123')
soup = BeautifulSoup(response.text, features="html.parser")
result = soup.find("p")


print(response)
print(response.text.split(""))
