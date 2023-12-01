import requests
from bs4 import BeautifulSoup

for page in range(1, 3):
    url = f"https://flatfy.ua/uk/%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6-" \
          f"%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%BA%D0%B8%D1%97%D0%B2?page={page}"
    response = requests.get(url)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, "lxml")
    data = soup.select('div.realty-preview__content-column')

    for item in data:
        price_elem = item.select_one('div.realty-preview-price.realty-preview-price--main')
        price = price_elem.text if price_elem else "Ціна не вказана"

        price_sqm_elem = item.select_one('div.realty-preview-price.realty-preview-price--sqm')
        price_for_sqmeter = price_sqm_elem.text if price_sqm_elem else "Ціна за м² не вказана"

        info_elems = item.select('span.realty-preview-info')

        area_info = next((info.text for info in info_elems if 'м²' in info.text), "Площа не вказана")
        rooms_info = next((info.text for info in info_elems if 'кімнат' in info.text),
                          "Інформація про кімнати не вказана")

        print(price + "\t\t" + price_for_sqmeter)
        print(rooms_info)
        print(area_info)
        print(50 * "_")
