# Python Web Scraping

```python
import requests
from bs4 import BeautifulSoup

url = "https://url.domain"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

page_numbers_text = soup.find(class_ = "css-class").text

```