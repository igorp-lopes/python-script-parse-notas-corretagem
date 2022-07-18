from dateutil.parser import parse


def extract_date_from_string(text):
    try:
        return parse(text, dayfirst=True)

    except ValueError:
        return
