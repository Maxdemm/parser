import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.work.ua/jobs/?ss=1"
r = requests.get(URL)
print(r.status_code)

soup = bs(r.text, "html.parser")
vacan_names = soup.find_all('h2', class_=True)
for name in vacan_names:
    if name.a and 'title' in name.a.attrs:
        print(name.a['title'])
        print('https://www.work.ua' + name.a['href'])
    else:
        print()

vacan_info = soup.find_all('p', class_="overflow text-muted add-top-sm cut-bottom")
for info in vacan_info:
    print(info.text)

