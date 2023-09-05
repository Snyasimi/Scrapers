import requests
from bs4 import BeautifulSoup

url = "https://www.gettyimages.com/search/2/image?family=creative&phrase=cow"
keyword = input('Input image keyword:\n')

url = f"https://www.gettyimages.com/search/2/image?family=creative&phrase={keyword}"
headers = {
 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
}

page = requests.get(url,headers=headers)

try:
 if page.status_code == 200:
  # print(page.text)
  soup = BeautifulSoup(page.text, 'html.parser')
  figures = soup.find_all('figure', limit=20)

  for figure in figures:
   images = figure.img
   tags = images.attrs
   image_src = tags['src']
   desc = tags['alt']
   print(f"\nIMAGE SRC : {image_src}\nIMAGE ALT : {desc}\n\n")
except e:
 print(f"There was an error {e}")

