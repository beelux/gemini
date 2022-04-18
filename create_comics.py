#!/usr/bin/env python3
from bs4 import BeautifulSoup

pageFile = open("website/dailybuild-comic.html", "r")
soup = BeautifulSoup(pageFile.read(), 'html5lib')
pageFile.close

file = open("comics.gmi", "w")

file.write("# dailybuild comic strips\n\n")

for element in soup.find_all('a', class_='fancybox'):
  print(element.get('title'))
  file.write("=> " + element.get('href') + " " + element.get('title') + "\n")

file.close() 
