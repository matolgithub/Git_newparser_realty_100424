import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://realty.ya.ru/kaluzhskaya_oblast/kupit/uchastok/?sort=DATE_DESC"


def make_response():
    header = Headers().generate()
    response = requests.get(url=url, headers=header)
    response_code = response.status_code
    print(response_code)
    page_text = response.text

    return page_text


def write_file():
    with open("file_ya_uchastki.txt", "w", encoding="UTF-8") as file:
        text = make_response()
        file.write(text)


def main():
    result_dict = {}
    num = 1
    html_text = make_response()
    soup = BeautifulSoup(html_text, "html.parser")
    all_data = soup.find_all("div",
                             class_="Gallery__activeImg-wrapper")
    for data in all_data:
        print(num, data)
        num += 1


if __name__ == "__main__":
    # make_response()
    # write_file()
    main()
