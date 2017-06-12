from winapi.models import API, Dll
import json
import hashlib


win8API = json.loads(open('/home/hcy/WinAPI/win8_v2', 'r').read())
for dll_name, api_info in win8API.items():
    print(dll_name)
    dll, create = Dll.objects.get_or_create(name=dll_name,)
    for api_name in api_info['ExportedFunctions']:
        api, created = API.objects.get_or_create(name=api_name,
                                                 hash_value=hashlib.sha256(api_name).hexdigest(),)
        if created:
            api.dll.add(dll)
            api.remark = 'win8 - ' + dll_name
        else:
            if 'win8' in api.remark:
                api.remark = '{0}, {1}'.format(api.remark, dll_name)
            else:
                api.remark = '{0}\nwin8 - {1}'.format(api.remark, dll_name)
        api.save()
