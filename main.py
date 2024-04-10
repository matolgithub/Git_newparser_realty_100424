import requests
import datetime
import random
from fake_headers import Headers
from bs4 import BeautifulSoup
from pprint import pprint
from PIL import Image

url = "https://kaluga.move.ru/kaluga/kvartiry/"


def test_requests():
    header = Headers().generate()
    response = requests.get(url=url, headers=header)
    response_code = response.status_code
    # print(response_code)
    page_text = response.text

    return page_text


def write_file():
    with open("file.txt", "w", encoding="UTF-8") as file:
        text = test_requests()
        file.write(text)


def main():
    result_dict = {}
    num = 1
    html_text = test_requests()
    soup = BeautifulSoup(html_text, "html.parser")
    all_id = soup.find_all("div", class_="search-item move-object")
    for item_id in all_id:
        id = item_id["data-id"]
        img_list = []
        # print(num, id)
        # num += 1
        for item_title in item_id:
            title = item_id.find("a", class_="search-item__title-link search-item__item-link")
            price = item_id.find("div", class_="search-item__price-values")
            img_link = item_id.find("div", class_="brazzers-photo-wrap brazzers-preloader")
            img_list.append(img_link["data-src"])
            result_dict[id] = {"title": f"{title.text}", "price": (f"{price.text}").strip(), "img": img_list}
    pprint(result_dict)


if __name__ == "__main__":
    # test_requests()
    # write_file()
    main()
