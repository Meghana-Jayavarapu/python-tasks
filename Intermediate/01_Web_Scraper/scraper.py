# ==========================================
# INTERMEDIATE TASK 1 - WEB SCRAPER
# ==========================================

import requests
from bs4 import BeautifulSoup


# Website URL
url = "https://books.toscrape.com/"


# Send request to website
response = requests.get(
    url,
    timeout=10
)


# Check if request was successful
response.raise_for_status()


# Convert HTML into BeautifulSoup object
soup = BeautifulSoup(
    response.text,
    "html.parser"
)


# Find all books
books = soup.select(
    "article.product_pod"
)


print("Books found:", len(books))

print("-" * 50)


# Extract information from each book
for book in books:

    title = book.h3.a["title"]

    price = book.select_one(
        ".price_color"
    ).get_text(strip=True)

    availability = book.select_one(
        ".availability"
    ).get_text(
        " ",
        strip=True
    )


    print("Title:", title)

    print("Price:", price)

    print("Availability:", availability)

    print("-" * 50)