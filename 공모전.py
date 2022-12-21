import requests
from bs4 import BeautifulSoup

rating_pages = []
pages = range(1, 1000)
for page in pages:
    url = "https://movie.naver.com/movie/point/af/list.naver?&page={}".format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    for i in soup.find_all("td", {"class":"title"}):
      rating_pages.append(i.get_text())

movies = []
for item in rating_pages:
  item_mod = item.replace("\t","")
  movies.append(item_mod)


semi_final = []
for item in movies:
  item_mod = item.replace("\n"," ")
  semi_final.append(item_mod)


final = []
for item in semi_final:
  item_mod = item.replace("신고 ","")
  final.append(item_mod)