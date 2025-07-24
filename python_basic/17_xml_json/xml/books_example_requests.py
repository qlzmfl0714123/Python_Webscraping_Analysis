import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://www.w3schools.com/xml/books.xml"
response = urllib.request.urlopen(url)	 # url 열기

xml_contents = str(response.read())
print(xml_contents)

soup = BeautifulSoup(xml_contents, "lxml") #lxml parser 호출
#
# #invention-title tag 찾기
title_tag = soup.find("title")
print (title_tag.get_text())

book1 = soup.find('book')
title_tag2 = book1.find('title')
print(title_tag2.get_text())

#{'valign':re.compile('top')}
book1 = soup.find('book',attrs={"category" : "cooking"}).find("author")
print(book1.get_text())

title_tag2 = soup.find('book').find('title')
print(title_tag2.get_text())


# title_tags = soup.find_all("title")
# for tag in title_tags:
#     print(tag.get_text())