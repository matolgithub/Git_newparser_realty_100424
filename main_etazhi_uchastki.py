import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://kaluga.etagi.com/realty_out/?trakt_id[]=1944&type[]=house&type[]=cottage&orderId=datecreatedesc"


def make_response():
    header = Headers().generate()
    response = requests.get(url=url, headers=header)
    response_code = response.status_code
    print(response_code)
    page_text = response.text

    return page_text


def write_file():
    with open("file_etazhi_uchastki.txt", "w", encoding="UTF-8") as file:
        text = make_response()
        file.write(text)


def main():
    result_dict = {}
    num = 1
    html_text = make_response()
    soup = BeautifulSoup(html_text, "html.parser")
    all_data = soup.find_all("div", class_="y8VEv templates-object-card etagiSlider__parent")
    for data in all_data:
        print(num, data.text)
        num += 1


if __name__ == "__main__":
    # make_response()
    # write_file()
    main()
