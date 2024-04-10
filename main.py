import requests
import datetime
import random
from fake_headers import Headers
from bs4 import BeautifulSoup

url = "https://kaluga.move.ru/kaluga/kvartiry/"


def test_requests():
    header = Headers().generate()
    response = requests.get(url=url, headers=header)
    response_code = response.status_code
    print(response_code)
    page_text = response.text

    return page_text


def write_file():
    with open("file.txt", "w", encoding="UTF-8") as file:
        text = test_requests()
        file.write(text)


def main():
    num = 1
    html_text = test_requests()
    soup = BeautifulSoup(html_text, "html.parser")
    all_title = soup.find_all("a", class_="search-item__title-link search-item__item-link")
    for item in all_title:
        print(num, item.text)
        num += 1


if __name__ == "__main__":
    # test_requests()
    # write_file()
    main()
