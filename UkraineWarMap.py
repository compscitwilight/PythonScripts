# script i use to get the link to an image of the russo-ukrainian war since i like geography

from requests import *
from bs4 import BeautifulSoup

response = get(
    url = "https://en.wikipedia.org/wiki/2022_Russian_invasion_of_Ukraine"
)

soup = BeautifulSoup(response.content, "html.parser")
map = soup.find(alt="2022 Russian invasion of Ukraine.svg")
mapImage = map["src"].replace("//", "")

print(mapImage)
