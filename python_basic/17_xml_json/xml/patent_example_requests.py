import urllib.request
from bs4 import BeautifulSoup

#with open("US08621662-20140107.XML", "r", encoding="utf8") as patent_xml:
#    xml = patent_xml.read()  # File을 String으로 읽어오기
url = "https://s3.ap-northeast-2.amazonaws.com/teamlab-gachon/US08621662-20140107.XML"
response = urllib.request.urlopen(url)	 # url 열기

xml_contents = str(response.read())
print(xml_contents)

soup = BeautifulSoup(xml_contents, "lxml") #lxml parser 호출
#
# #invention-title tag 찾기
invention_title_tag = soup.find("invention-title")
print (invention_title_tag.get_text())
