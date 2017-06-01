from winapi.models import API, Dll
import re


with open('/home/hcy/WinAPI/mimikatz.exe_3584.trace.calls', 'r') as f:
    pat = '::(.*)@ EIP'
    for line in f.readlines():
        api_name = re.findall(pat, line)[0].strip()
        _api = API.objects.filter(name=api_name)
        if len(_api) == 0:
            print(api_name)
