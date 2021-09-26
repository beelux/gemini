import requests
from bs4 import BeautifulSoup
page = requests.get("https://dailybuild.org/dailybuild-comic.html")
soup = BeautifulSoup(page.content, 'html5lib')

file = open("comics.gmi", "w")

file.write("# dailybuild comic strips\n\n")

for element in soup.find_all('a', class_='fancybox'):
  file.write("=> " + element.get('href') + " " + element.get('title') + "\n")

file.close() 
