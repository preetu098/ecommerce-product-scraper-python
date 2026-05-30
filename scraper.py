"""
E-Commerce Product Scraper

Author: Pratibha Rajawat
Description:
Scrapes book data from BooksToScrape and exports results to CSV.

Technologies:
- Requests
- BeautifulSoup
- Pandas
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "lxml")

    books = soup.find_all("article", class_="product_pod")

    data = []

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        rating=book.find("p")['class'][1]

        product_url=url+book.h3.a["href"]

        data.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating":rating,
            "Product URL":product_url
        })

    df = pd.DataFrame(data)

    df.to_csv(
        "data/books.csv",
        index=False,
        encoding="utf-8"
    )

    print("Data saved successfully!")

else:
    print("Failed to fetch webpage")