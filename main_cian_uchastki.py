import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://kaluga.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=3&offer_seller_type%5B0%5D=2&offer_type=suburban&region=4576"


def make_response():
    header = Headers().generate()
    response = requests.get(url=url, headers=header)
    response_code = response.status_code
    print(response_code)
    page_text = response.text

    return page_text


def write_file():
    with open("file_cian_uchastki.txt", "w", encoding="UTF-8") as file:
        text = make_response()
        file.write(text)


def main():
    result_dict = {}
    num = 1
    html_text = make_response()
    soup = BeautifulSoup(html_text, "html.parser")
    all_data = soup.find_all("article", class_="_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc")
    for all_item in all_data:
        total_info = []
        object_address = ""
        price = soup.find("span",
                          class_="_93444fe79c--color_black_100--Ephi7 _93444fe79c--lineHeight_28px--KFXmc _93444fe79c--fontWeight_bold--BbhnX _93444fe79c--fontSize_22px--sFuaL _93444fe79c--display_block--KYb25 _93444fe79c--text--e4SBY _93444fe79c--text_letterSpacing__normal--tfToq")
        title = soup.find("span",
                          class_="_93444fe79c--color_black_100--Ephi7 _93444fe79c--lineHeight_22px--FdvaW _93444fe79c--fontWeight_bold--BbhnX _93444fe79c--fontSize_16px--QNYmt _93444fe79c--display_block--KYb25 _93444fe79c--text--e4SBY _93444fe79c--text_letterSpacing__normal--tfToq")
        total_info.append(f"{all_item.text} ")
        # address_list = soup.find_all("a", class_="_93444fe79c--link--NQlVc")
        print(num, total_info)
        num += 1


if __name__ == "__main__":
    # make_response()
    # write_file()
    main()
