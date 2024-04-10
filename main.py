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
    pass


if __name__ == "__main__":
    # test_requests()
    write_file()
    main()
