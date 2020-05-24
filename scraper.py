__author__ = "hpost2019"

import sys
import requests
import re


def parse_url(response):
    """Accepts response from requests and parses response
    for information from website"""
    found_url = re.findall(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        , response.text)
    print("URLs:\n")
    for url in found_url:
        print(url)


def main(args):
    if len(args) != 1:
        print('usage: python scraper.py url (ex: https://kenzie.academy')
        sys.exit(1)

    website = args[0]
    try:
        response = requests.get(website)
        parse_url(response)
    except requests.ConnectionError as exception:
        print('Please enter a valid url or make sure website exists\n')
        print(exception, '\n')
        print('usage: python scraper.py url (ex: https://kenzie.academy')
        sys.exit(2)


if __name__ == '__main__':
    main(sys.argv[1:])
