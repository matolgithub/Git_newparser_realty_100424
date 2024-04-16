import time
import json

import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
from pprint import pprint


def make_response():
    # limit=10 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    url = f"https://kaluga.move.ru/kaluga/kvartiry/vtorichnaya/?limit=100&rooms%5B%5D=-1&rooms%5B%5D=1&rooms%5B%5D=2&rooms%5B%5D=3"
    header = Headers().generate()
    response = requests.get(url=url, headers=header)
    response_code = response.status_code
    # print(response_code)
    page_text = response.text

    return page_text


def make_response_2(page_number):
    # url = f"https://kaluga.move.ru/kaluga/kvartiry/vtorichnaya/?page={page_number}&rooms%5B0%5D=-1&rooms%5B1%5D=1&rooms%5B2%5D=2&rooms%5B3%5D=3"
    # &limit=100 лимит поставил 10 вместо 100 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    url = f"https://kaluga.move.ru/kaluga/kvartiry/vtorichnaya/?page={page_number}&limit=100&rooms%5B%5D=-1&rooms%5B%5D=1&rooms%5B%5D=2&rooms%5B%5D=3"
    header = Headers().generate()
    response = requests.get(url=url, headers=header)
    page_text = response.text

    return page_text


def make_page_response(url):
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
        "Price_mkv": "",
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
        "Characteristics: Полный адрес": "",
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
        "Characteristics: инфо о доме": "",
        "Weight": "",
        "Length": "",
        "Width": "",
        "Height": "",
        "SEO title": "квартиры в калуге",
        "SEO descr": "купить квартиру, недвижимость в калуге",
        "SEO keywords": "квартиры в калуге, купить квартиру в калуге, квартиры в калуге вторичка, купить квартиру в калуге недорого",
        "FB title": "квартиры в калуге",
        "FB descr": "купить квартиру, недвижимость в калуге",
        "Url": "",
        "Url_page": ""
    }

    return id_dict


def main():
    result_dict = {}
    # pages = page_count()   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    pages = 1  # сократил пагинацию, потом убрать!
    num = 2
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
            description = data_id.find("span", class_="black-text").text
            id_dict["Description"] = description.strip()
            city = data_id.find("li", class_="search-item__item-property search-item__location").text
            id_dict["Characteristics: Город"] = city.strip()
            etazh = (data_id.find_all("li", class_="search-item__item-property"))[1].text
            id_dict["Characteristics: Этаж"] = etazh.strip()
            square = (data_id.find_all("li", class_="search-item__item-property"))[2].text
            id_dict["Characteristics: Общая площадь"] = square.strip()
            rooms = (data_id.find_all("li", class_="search-item__item-property"))[3].text
            id_dict["Characteristics: rooms_count"] = rooms.strip()
            category = f"{(rooms.strip())[-1]}-комнатная квартира"
            id_dict["Category"] = category
            author_type = data_id.find("li", class_="search-item__item-property search-item__provider").text
            id_dict["Characteristics: Продавец"] = author_type.strip()
            price = data_id.find("div", class_="search-item__price-values").text
            id_dict["Price"] = price.strip()
            img_list = []
            img = data_id.find_all("div", class_="brazzers-photo-wrap")
            for img_item in img:
                image = img_item.get("data-src")
                if image != None:
                    if image[:6] != "https:":
                        image = f"https:{image}"
                    img_list.append(image)
            id_dict["Photo"] = img_list

            page_link = data_id.find("a", class_="search-item__title-link search-item__item-link")
            url_page = page_link.get("href")
            if url_page[:6] != "https:":
                url_page = f"https:{url_page}"
            id_dict["Url_page"] = url_page

            response_page = make_page_response(url_page)
            soup = BeautifulSoup(response_page, "html.parser")
            data_page = (soup.find("div", class_="object-page__text-block")).text.strip()
            # print(data_page)
            id_dict["Text"] = data_page

            price_mkv = (soup.find("span", class_="block-price_second-price-value js-price-second-value")).text.strip()
            id_dict["Price_mkv"] = price_mkv

            town = (soup.find("a", class_="geo-block__geo-info_link"))
            id_dict["Characteristics: Город"] = town.get("title")

            street = (soup.find_all("a", class_="geo-block__geo-info_link"))[1]
            id_dict["Characteristics: Улица"] = street.get("title")

            type_obj = soup.find_all("div", class_="object-info__details-table_property_value")[5]
            id_dict["Characteristics: Тип объекта"] = type_obj.text.strip()

            type_nedv = soup.find_all("div", class_="object-info__details-table_property_value")[6]
            id_dict["Characteristics: Тип недвижимости"] = type_nedv.text.strip()

            zhil_pl = soup.find_all("div", class_="object-info__details-table_property_value")[8]
            id_dict["Characteristics: Жилая площадь"] = zhil_pl.text.strip()

            kuh_pl = soup.find_all("div", class_="object-info__details-table_property_value")[9]
            id_dict["Characteristics: Площадь кухни"] = kuh_pl.text.strip()

            remont = soup.find_all("div", class_="object-info__details-table_property_value")[14]
            id_dict["Characteristics: Ремонт"] = remont.text.strip()

            result_dict[data_id["data-id"]] = id_dict
            num += 1
        # time.sleep(0.05)
        print(f"Обработана {page_number} страница.")

    pprint(result_dict)
    with open('result.json', 'w', encoding="UTF-8") as fp:
        json.dump(result_dict, fp, ensure_ascii=False)


if __name__ == "__main__":
    # make_response()
    # write_file()
    # page_count()
    main()
