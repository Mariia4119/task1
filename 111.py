# import requests
# link = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
# r = requests.get(link).json()
# for el in r:
#     if el['cc'] == "USD":
#         print(el['rate'])

# import requests
# link = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange'
# params = {'date': '20211022',
#                    'json': 'json'
#         }
# r = requests.get(link, params=params).json()
# for el in r:
#      if el['cc'] == "USD":
#          print(el['rate'])

import requests
from datetime import datetime, timedelta
link = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange'
all_info = []
date = datetime.now()
for i in range(365):
    params = {'date': date.strftime('%Y%m%d'),
                    'json': 'json'
         }
    r = requests.get(link, params=params).json()
    all_info.extend(r)
    date -= timedelta(days=1)
print(all_info)

