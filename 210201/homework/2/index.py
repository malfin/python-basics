# Не доделано.

import re
import requests

RE_DATA_VALIDATOR = re.compile(r'^(\d{2}[./-]){2}\d{4}$')


def data_is_valid(data):
    return RE_DATA_VALIDATOR.match(data)


RE_XLS_FILE = re.compile(r'href="([^"]+\.xls)"')

request_url = 'https://kpk.kss45.ru/%D1%83%D1%87%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0' \
              '/%D1%80%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BF%D0%B0%D1%80.html '

response = requests.get(request_url)
content = response.content.decode(encoding=response.encoding)

parsed = RE_XLS_FILE.findall(content)
parsed = filter(lambda x: x.endswith('.xls'), parsed)

print(*parsed, sep='\n\n')


def get_timetable(first_date):
    return data_is_valid(first_date)


get_timetable('02.2020')

