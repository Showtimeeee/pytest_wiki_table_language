import requests
from bs4 import BeautifulSoup
from typing import List
from dataclasses import dataclass
import re


@dataclass
class ProgrammingLanguage:
    name: str
    frontend: str
    backend: str
    popularity: int


url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table", {"class": "wikitable"})

data = []
for row in table.find_all("tr")[1:]:
    columns = row.find_all(["th", "td"])
    name = columns[0].text.strip()

    if columns[1].find("a"):
        frontend = columns[1].find("a").text.strip()
    else:
        frontend = columns[1].text.strip()

    if columns[2].find("a"):
        backend = columns[2].find("a").text.strip()
    else:
        backend = columns[2].text.strip()

    popularity_text = columns[3].text.strip().replace(",", "")
    try:
        popularity = int(popularity_text.split()[0])
    except (IndexError, ValueError):
        popularity = 0

    popularity_text = columns[3].text.strip().replace(",", "")

    # взять все цифры из строки
    popularity = re.sub(r'\D', '', popularity_text)

    if popularity:
        popularity = int(popularity)
    else:
        popularity = 0

    data.append(ProgrammingLanguage(name, frontend, backend, popularity))

