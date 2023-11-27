import requests
from bs4 import BeautifulSoup as bs

url = "https://www.work.ua/jobs/?ss=1"
r = requests.get(url)
print(r.status_code)

soup = bs(r.text, "html.parser")
vacan_names = soup.find_all('h2', class_=True)
vacan_info = soup.find_all('p', class_="overflow text-muted add-top-sm cut-bottom")

for i in range(len(vacan_names)):
    name = vacan_names[i]
    if name.a and 'title' in name.a.attrs:
        print(name.a['title'])
        print('https://www.work.ua' + name.a['href'])
        info = vacan_info[i]
        print(info.text)
        print("_" * 150)



