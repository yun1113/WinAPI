from bs4 import BeautifulSoup
import requests
import datetime
import json

url = 'http://www.geoffchappell.com/studies/windows/win32/apisetschema/history/sets61.htm'
session = requests.Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
sourse_code = session.get(url).text
soup = BeautifulSoup(sourse_code, "html.parser")

row_list = soup.select('.Functions tr')

url_list = []
# with open('win7-apiset-list', 'w') as f:
for r in row_list:
    if r.select('td'):
        url_list.append(r.select('a')[0]['href'])
            # f.write('{0}\n'.format(r.select('a')[0]['href']))
# import pdb;pdb.set_trace()

url_list = ['http://www.geoffchappell.com/studies/windows/win32/apisetschema/' + url[3:] for url in url_list]
api_dict = {}

for u in url_list:
    sourse_code = session.get(u).text
    soup = BeautifulSoup(sourse_code, "html.parser")
    api_set_name = soup.select('h1')[0].getText()
    api_list = [api.getText() for api in soup.select('.function')]
    api_dict[api_set_name] = api_list

json.dump(api_dict, open("win32_win7",'w'))
