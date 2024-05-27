# Automate the extraction of data from websites.
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

url = 'https://www.google.com/'
data = scrape_website(url)
print(data.prettify())
