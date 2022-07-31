from dateutil.parser import parse
from re import match, search


def extract_date_from_string(text):
    try:
        return parse(text, dayfirst=True)

    except ValueError:
        return


def extract_from_string_using_regex(text, regex):
    try:
        return search(regex, text).group()
    except ValueError:
        return None
