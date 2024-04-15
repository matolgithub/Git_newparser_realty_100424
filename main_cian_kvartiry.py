import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://kaluga.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&region=4780&room1=1&room2=1&room3=1"


def make_response():
    header = Headers().generate()
    response = requests.get(url=url, headers=header)
    response_code = response.status_code
    print(response_code)
    page_text = response.text

    return page_text


def write_file():
    with open("file_cian_kvart.txt", "w", encoding="UTF-8") as file:
        text = make_response()
        file.write(text)


def main():
    result_dict = {
        "Tilda UID": "", "Brand": "", "SKU": "", "Mark": "", "Category": "", "Title": "", "Description": "", "Text": "",
        "Photo": [],
        "Price": "",
        "Quantity": "",
        "Price": "",
        "Old": "",
        "Editions": "",
        "Modifications": "",
        "External": "",
        "ID": "",
        "Parent UID": "",
        "Characteristics: Площадь": "",
        "Characteristics: accommodation_type": "",
        "Characteristics: author_type": "",
        "Characteristics: deal_type": "",
        "Characteristics: location": "",
        "Characteristics: district": "",
        "Characteristics: street": "",
        "Characteristics: house_number": "",
        "Characteristics: floor": "",
        "Characteristics: floors_count": "",
        "Characteristics: price": "",
        "Characteristics: residential_complex": "",
        "Characteristics: rooms_count": "",
        "Characteristics: total_meters": "",
        "Characteristics: Тип недвижимости": "",
        "Characteristics: Тип объекта": "",
        "Characteristics: Тип сделки": "",
        "Characteristics: Продавец": "",
        "Characteristics: Количество комнат": "",
        "Characteristics: ЖК": "",
        "Characteristics: Город": "",
        "Characteristics: Район": "",
        "Characteristics: Улица": "",
        "Characteristics: Номер дома": "",
        "Characteristics: Этаж": "",
        "Characteristics: Всего этажей в доме": "",
        "Characteristics: Общая площадь": "",
        "Characteristics: Жилая площадь": "",
        "Characteristics: Площадь кухни": "",
        "Characteristics: Ремонт": "",
        "Characteristics: Год постройки": "",
        "Characteristics: Тип строения": "",
        "Characteristics: Лифты": "",
        "Characteristics: Перекрытия": "",
        "Characteristics: Количество подъездов": "",
        "Characteristics: Аварийность": "",
        "Characteristics: Обременения": "",
        "Weight": "",
        "Length": "",
        "Width": "",
        "Height": "",
        "SEO title": "",
        "SEO descr": "",
        "SEO keywords": "",
        "FB title": "",
        "FB descr": "",
        "Url": ""
    }
    num = 1
    html_text = make_response()
    soup = BeautifulSoup(html_text, "html.parser")
    all_data = soup.find_all("article", class_="_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc")


if __name__ == "__main__":
    # make_response()
    # write_file()
    main()
