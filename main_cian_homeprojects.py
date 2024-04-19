import requests
from bs4 import BeautifulSoup
import json
from fake_headers import Headers
import math
from pprint import pprint


def make_header():
    header = Headers().generate()

    return header


def make_response(url) -> str:
    header = make_header()
    response = requests.get(url=url, headers=header)
    page_text = response.text

    return page_text


def make_soup(url):
    html_text = make_response(url)
    soup = BeautifulSoup(html_text, "html.parser")

    return soup


def count_page(url) -> int:
    soup = make_soup(url)
    count_objects = soup.find("div", class_="_4e5f713ae4--container--PbciU")
    pages = count_objects.find_all("span")
    list_text = []
    for item in pages:
        list_text.append(item.text)
    total_obj = int(list_text[1].split(" ")[1])
    pages = math.ceil(total_obj / 28)

    return pages


def make_url_pages(url) -> list:
    pages = count_page(url)
    url_pages_list = []
    url_2 = url
    for page_number in range(1, pages + 1):
        if page_number > 1:
            url_2 = f"{url}&page={page_number}"
        url_pages_list.append(url_2)
        url_2 = url
    # pprint(url_pages_list)

    return url_pages_list


def make_object_links(url) -> list:
    url_object_list = []
    num = 1
    pages_link = make_url_pages(url)
    soup = make_soup(url)
    for page_link in pages_link:
        objects_link = soup.find_all("div", class_="_4e5f713ae4--container--ktXmQ _4e5f713ae4--container--H8jRD")
        for object_link in objects_link:
            link = object_link.find("a", class_="_4e5f713ae4--link--acwir")
            url_object = f'https://kaluga.cian.ru{link.get("href")}'
            url_object_list.append(url_object)
            num += 1
    # pprint(url_object_list)

    return url_object_list


def main():
    make_object_links("https://kaluga.cian.ru/country-builders-projects/?utm_medium=menu&utm_content=banner")


if __name__ == "__main__":
    main()
