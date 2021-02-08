import requests
import re

# RE_NAME = re.compile(r'Расписание на.+.xls')
RE_NAME = re.compile(r'href="([^"]+\.xls)"')


# https://kpk.kss45.ru/attachments/article/2759/Расписание на 1-6 февраля по группам3.xls

request_url = 'https://kpk.kss45.ru/%D1%83%D1%87%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0/%D1%80%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BF%D0%B0%D1%80.html'

response = requests.get(request_url)

content = response.content.decode(encoding=response.encoding)
parse = RE_NAME.findall(content)
# parse = filter(lambda x: x.endswith('.xls"'), parse)
# print(len(list(parse)))
print(*parse, sep='\n\n')
