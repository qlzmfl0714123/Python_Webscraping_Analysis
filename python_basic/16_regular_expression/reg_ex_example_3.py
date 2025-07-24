import urllib.request # urllib 모듈 호출
import re

base_url = "http://web.eecs.umich.edu/~radev/coursera-slides/" #url 값 입력
html = urllib.request.urlopen(base_url)	 # url 열기
html_contents = str(html.read().decode("utf8"))  # html 파일 읽고, 문자열로 변환
# print(html_contents )
url_list = re.findall(r"nlp[0-9a-zA-Z\_\.]*\.pdf", html_contents)

#테스트 하기 위해 3건만 가져옴
url_list2 = url_list[:3]

for url in url_list2:
    file_name = "".join(url)
    full_url = base_url + file_name
    print(full_url)
    fname, header = urllib.request.urlretrieve(full_url, file_name)
    print ("End Download",fname," ",header)