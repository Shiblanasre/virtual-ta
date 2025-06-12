import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "Mozilla/5.0"
}

url = "https://discourse.onlinedegree.iitm.ac.in/c/tds-jan-2025/315"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Add your logic to extract links and content here

print("Scraping complete.")
