import requests
from bs4 import BeautifulSoup
def download_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content.decode('utf-8')
        print("Downloaded content.")
        return content
    else:
        print(f"Failed to download the page. Status code: {response.status_code}")
        return None

if __name__ == '__main__':
    url = "https://www.work.ua/jobs/?ss=1"
    content = download_url(url)

    if content is None:
        print("ERROR: CONTENT_IS_NONE")

    soup = BeautifulSoup(content, 'html.parser')
    vacancy_names = soup.select('h2 a[title]')
    vacancy_info = soup.select('p.overflow.text-muted.add-top-sm.cut-bottom')

    for i in range(len(vacancy_names)):
        name = vacancy_names[i]
        info = vacancy_info[i]
        print(name['title'])
        print('https://www.work.ua' + name['href'])
        print(info.text)

        print("_" * 150)



