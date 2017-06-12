from winapi.models import API, Dll
import re
import json
import os


def generate_data(filename):
    with open(filename, 'r') as f:
        dll_pat = '-> (.*)::'
        api_pat = '::(.*)@ EIP'

        data = []
        _dll = set(dll.name for dll in Dll.objects.all())
        _api = set(api.name for api in API.objects.all())

        for line in f.readlines():

            dll_name = re.findall(dll_pat, line)[0].strip()
            api_name = re.findall(api_pat, line)[0].strip()

            if dll_name in _dll and api_name in _api:
                data.append([dll_name, api_name])

    json.dump(data, open(os.path.basename(filename)+'.json', 'w'))


def run(*args):
    generate_data(args[0])

# python manage.py runscript check_api_in_db --script-args /home/hcy/WinAPI/mimikatz.exe_3584.trace.calls