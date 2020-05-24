__author__ = "hpost2019"

import sys
import requests
import re


def print_lists(title, print_list):
    """prints lists that are passed in with title"""
    print(title, '\n')
    for item in print_list:
        print(item)
    print('\n')
    pass


def remove_dups(my_list):
    """removes duplicates from lists"""
    results = []
    for item in my_list:
        if item not in results:
            results.append(item)
    return results


def find_url(page_text):
    """uses passed in text and finds all urls listed"""
    found_urls = re.findall(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|"
        r"[$-_@.&+]|[!*\(\),]|"
        r"(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        page_text)
    if found_urls:
        print_lists('URLs:', remove_dups(found_urls))
    else:
        print_lists('URLs:', ["None"])
    pass


def find_emails(page_text):
    found_email = re.findall(
        r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",
        page_text)
    if found_email:
        print_lists('EMAILS:', remove_dups(found_email))
    else:
        print_lists('EMAILS:', ["None"])
    pass


def find_phone_numbers(page_text):
    found_phone_nums = re.findall(
        r"1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})"
        r"\W*([0-9]{4})(\se?x?t?(\d*))?",
        page_text)
    if found_phone_nums:
        print_lists('PHONE NUMBERS:', remove_dups(found_phone_nums))
    else:
        print_lists('PHONE NUMBERS:', ["None"])


def parse_url(response):
    """Accepts response from requests and parses response
    for information from website"""
    find_url(response.text)
    find_emails(response.text)
    find_phone_numbers(response.text)


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
