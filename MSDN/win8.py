from bs4 import BeautifulSoup
import requests
import datetime
import json

url = 'https://msdn.microsoft.com/zh-tw/library/windows/desktop/dn505783(v=vs.85).aspx'
sourse_code = requests.get(url).text

with open('win8-source-code', 'w') as f:
    f.write(sourse_code.encode('utf8'))

soup = BeautifulSoup(sourse_code, "html.parser")

row_list = soup.select('table tr')
# import pdb;pdb.set_trace()

winAPI = {}
api_count = 0
for row in row_list:
    if row.select('[data-th]'):
        row_data = row.select('[data-th]')
        api_set = row_data[0].getText()
       
        api_list = []
        for api in row_data[1].select('p'):
            api_list.append(api.getText().strip())
       
        if api_set in winAPI.keys():
            for a in api_list:
                if a not in winAPI[api_set]:
                    winAPI[api_set].append(a)
                    api_count += 1
        else:
            winAPI[api_set] = api_list
            api_count += len(api_list)
print(api_count)
print(len(winAPI.keys()))
json.dump(winAPI, open("win8API",'w'))
