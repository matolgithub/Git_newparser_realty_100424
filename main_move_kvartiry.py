import time

import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
from pprint import pprint


def make_response():
    url = f"https://kaluga.move.ru/kaluga/kvartiry/vtorichnaya/?limit=100&rooms%5B%5D=-1&rooms%5B%5D=1&rooms%5B%5D=2&rooms%5B%5D=3"
    header = Headers().generate()
    response = requests.get(url=url, headers=header)
    response_code = response.status_code
    # print(response_code)
    page_text = response.text

    return page_text


def make_response_2(page_number):
    # url = f"https://kaluga.move.ru/kaluga/kvartiry/vtorichnaya/?page={page_number}&rooms%5B0%5D=-1&rooms%5B1%5D=1&rooms%5B2%5D=2&rooms%5B3%5D=3"
    url = f"https://kaluga.move.ru/kaluga/kvartiry/vtorichnaya/?page={page_number}&limit=100&rooms%5B%5D=-1&rooms%5B%5D=1&rooms%5B%5D=2&rooms%5B%5D=3"
    header = Headers().generate()
    response = requests.get(url=url, headers=header)
    page_text = response.text

    return page_text


def write_file():
    with open("file_move_kvart.txt", "w", encoding="UTF-8") as file:
        text = make_response()
        file.write(text)


def get_response():
    html_text = make_response()
    soup = BeautifulSoup(html_text, "html.parser")

    return soup


def page_count():
    soup = get_response()
    all_data = soup.find_all("a", class_="pagination-block__page-link")
    for data in all_data:
        pages = (data.text).strip()
    paginator = int(pages)
    # print(paginator, type(paginator))

    return paginator


def get_id_dict():
    id_dict = {
        "Tilda UID": "",
        "Brand": "",
        "SKU": "",
        "Mark": "",
        "Category": "",
        "Title": "",
        "Description": "",
        "Text": "",
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

    return id_dict


def main():
    result_dict = {}
    # pages = page_count()   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    pages = 10  # сократил пагинацию, потом убрать!
    num = 1
    for page_number in range(1, pages + 1):
        html_text = make_response()
        if page_number > 1:
            html_text = make_response_2(page_number)
        soup = BeautifulSoup(html_text, "html.parser")
        all_data = soup.find_all("div", class_="search-item move-object")
        for data_id in all_data:
            id_dict = get_id_dict()
            id_dict["SKU"] = data_id["data-id"]
            id_dict["Tilda UID"] = f"KV-{num}"
            title = data_id.find("a", class_="search-item__title-link search-item__item-link").text
            id_dict["Title"] = title
            # print(num, data_id["data-id"], title)
            result_dict[data_id["data-id"]] = id_dict
            num += 1
        time.sleep(0.2)
        print(f"Обработана {page_number} страница.")
    pprint(result_dict)


if __name__ == "__main__":
    # make_response()
    # write_file()
    # page_count()
    main()
