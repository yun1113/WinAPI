from bs4 import BeautifulSoup
import requests
import datetime
import json

url = 'http://geoffchappell.com/studies/windows/win32/ntdll/history/names62.htm?tx=2,6'
session = requests.Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
sourse_code = session.get(url).text
soup = BeautifulSoup(sourse_code, "html.parser")

row_list = soup.select('table tr')

api_set_list = []
for r in row_list:
    if r.select('td'):
        api_set_list.append(r.select('td')[0].getText())

print(len(api_set_list))
json.dump(api_set_list, open("ntdll_api_win8",'w'))
