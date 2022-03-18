# Downloads all images from a page

import requests
import urllib.request
from bs4 import BeautifulSoup

link = "link here"
fetchResponse = requests.get(
    url=link
)

soup = BeautifulSoup(fetchResponse.content, "html.parser")
allImages = soup.find_all("img")
allImageLinks = []

for img in allImages:
    allImageLinks.append(img["src"])

for i in range(len(allImageLinks)):
    fileName = "{}.png".format(str(i))
    image = urllib.request.urlretrieve(allImageLinks[i], fileName)
