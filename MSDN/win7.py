from bs4 import BeautifulSoup
import requests
import datetime
import json

url = 'https://msdn.microsoft.com/en-us/library/windows/desktop/hh920509(v=vs.85).aspx'
sourse_code = requests.get(url).text
soup = BeautifulSoup(sourse_code, "html.parser")

row_list = soup.select('#mainSection ul li')

url_list = []
with open('win7-url-list', 'w') as f:
    for r in row_list:
        url_list.append(r.select('a')[0]['href'])
        f.write('{0}\n'.format(r.select('a')[0]['href']))
# import pdb;pdb.set_trace()

for u in url_list:
    sourse_code = requests.get(url).text
    soup = BeautifulSoup(sourse_code, "html.parser")

    row_list = soup.select('#mainSection ul li')

# winAPI = {}
# api_count = 0
# for row in row_list:
#     if row.select('[data-th]'):
#         row_data = row.select('[data-th]')
#         api_set = row_data[0].getText()
       
#         api_list = []
#         for api in row_data[1].select('p'):
#             api_list.append(api.getText().strip())
       
#         if api_set in winAPI.keys():
#             for a in api_list:
#                 if a not in winAPI[api_set]:
#                     winAPI[api_set].append(a)
#                     api_count += 1
#         else:
#             winAPI[api_set] = api_list
#             api_count += len(api_list)
# print(api_count)
# print(len(winAPI.keys()))
# json.dump(winAPI, open("win8API",'w'))
