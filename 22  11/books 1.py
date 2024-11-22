import requests
from bs4 import BeautifulSoup

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
page = 1
books = []

while True:
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    book_list = soup.select('article.product_pod')
    if not book_list:
        break

    for book in book_list:
        title = book.h3.a['title']
        price = book.select_one('p.price_color').text
        books.append((title, price))

    page += 1

for title, price in books:
    print(f"Title: {title}, Price: {price}")
