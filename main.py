import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(long_url, headers):
    params = {"long_url": long_url}
    shorten_url = "https://api-ssl.bitly.com/v4/shorten"
    response = requests.post(shorten_url, json=params, headers=headers)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(bitlink, headers):
    clicks_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    response = requests.get(clicks_url, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(bitlink, headers):
    сhecking_abbreviated_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
    response = requests.get(сhecking_abbreviated_url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Сокращение ссылок с помощю 'bitli.com' и вывос количества переходов по сокращённой ссылке")
    parser.add_argument("link", help="укажиите ссылку на сайт")
    args = parser.parse_args()
    try:
        bitly_token = os.getenv('BITLY_TOKEN')
        headers = {'Authorization': f"Bearer {bitly_token}"}
        user_url = args.link

        analytics_link = urlparse(user_url)
        bitlink = f"{analytics_link.netloc}{analytics_link.path}"

        if is_bitlink(bitlink, headers):
            print("Количество кликов:", count_clicks(bitlink, headers))

        else:
            short_link = shorten_link(user_url, headers)
            print("сокращённая ссылка: ", short_link)

    except requests.exceptions.HTTPError:
        print("ошибка неправельная ссылка")


if __name__ == "__main__":
    main()
